import os
from flask import Flask, request, render_template, session, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.booking_repository import BookingRepository
from lib.booking import Booking
import phonenumbers
import re
from flask_mail import Mail, Message
from lib.confirmation import send_text_confirmation
from dotenv import load_dotenv
load_dotenv()

# Create a new Flask app
app = Flask(__name__)
app.config['MAIL_SERVER'] = 'smtp-mail.outlook.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
mail = Mail(app)

# == Your Routes Here ==

# GET /
# Returns the homepage

@app.route('/', methods=['GET'])
def get_index():
    user_id = session.get('user_id')
    if user_id:
        return app.redirect('/spaces')
    else:
        return app.redirect('/login')

@app.route('/confirmation/<id>', methods = ['GET'])
def confirmation(id):
    connection = get_flask_database_connection(app)
    user_id = session.get('user_id')
    user_repository = UserRepository(connection)
    space_repository = SpaceRepository(connection)
    user = user_repository.find_user_with_bookings(user_id)
    booking_repository = BookingRepository(connection)
    booking = booking_repository.find(id)
    spaces = space_repository.all()
    return render_template('confirmation.html',booking=booking, user=user, space=spaces)



@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    spaces = space_repository.all()
    user_id = session.get('user_id')
    if user_id:
        user_repository = UserRepository(connection)
        user = user_repository.find(user_id)
        return render_template('spaces.html', user=user, spaces=spaces)
    else:
        return app.redirect('/')
    
@app.route('/spaces/<int:id>', methods=['GET'])
def get_space_by_id(id):
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    space = space_repository.find(id)
    user_id = session.get('user_id')
    if user_id:
        user_repository = UserRepository(connection)
        user = user_repository.find(user_id)
    if space:
        return render_template('space.html', space=space, user=user)
    else:
        return "Space not found", 404  # Return a 404 status if space is not found

@app.route('/spaces/<int:id>', methods=['POST'])
def book_new_request(id):
    connection = get_flask_database_connection(app)
    space_repository = SpaceRepository(connection)
    user_id = session.get('user_id')
    space_id = id
    space = space_repository.find(space_id)
    date = request.form.get('date')
    booking_repo = BookingRepository(connection)
    booking = Booking(None, date, date, space.price, user_id, space_id)
    booking_repo.create(booking)
    user_repository = UserRepository(connection)
    user = user_repository.find(user_id)
    user_email = session.get('user_email')
    if request.method == 'POST':
        msg = Message(subject='Your Booking Request is Submitted!', sender='makers.bnb@outlook.com', recipients=[user_email])
        msg.body = f"""
We've received your booking request and it's now waiting for the host's confirmation. We'll notify you as soon as we get a response. Thanks for choosing Makers BnB!

Best Regards,
MakersBnB Team"""
        mail.send(msg)
    return app.redirect('/requests')


@app.route('/spaces/new')
def spaces():
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = user_repository.find(user_id)
    return render_template('list.html', user=user)

@app.route('/spaces/new', methods=['POST'])
def post_list():
    connection = get_flask_database_connection(app)
    name = request.form['name']
    addressline = request.form['addressline']
    city = request.form['city']
    postcode = request.form['postcode']
    address = f"{addressline}, {city}, {postcode}"
    price = request.form['price']
    description = request.form['description']
    image_url = request.form['image']
    # start_date = request.form['start_date']
    # end_date = request.form['end_date']
    user_id = request.form['user_id']
    space_repository = SpaceRepository(connection)
    new_space = Space(None, name, address, price, description, user_id, image_url)
    space_repository.create(new_space)
    
    
    if request.method == 'POST':
            user_id = session.get('user_id')
            user_email = session.get('user_email')
            msg = Message(subject=f'{name} is Live on Makers BnB!', sender='makers.bnb@outlook.com', recipients=[user_email])
            msg.body = f"""
Congratulations! {name} is now live on Makers BnB. We're excited to see how guests will love your space. If you have any questions or need assistance, feel free to reach out to us.

Best Regards,
MakersBnB Team"""
            
            mail.send(msg)
    return app.redirect('/spaces')

@app.route('/requests')
def requests():
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = user_repository.find_with_spaces_and_bookings(user_id)
    booking_repository = BookingRepository(connection)
    for space in user.spaces:
        x = booking_repository.find_by_space_id(space)
    return render_template('requests.html', user=user)

@app.route('/confirm/<id>', methods=['GET'])
def confirm(id):
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    booking = booking_repository.find(id)
    user_repository = UserRepository(connection)
    user = user_repository.find(user_id)
    booking_repository.confirm(booking)
    send_text_confirmation(booking, user)
    return app.redirect('/requests')

@app.route('/reject/<id>', methods=['GET'])
def reject(id):
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    booking_repository = BookingRepository(connection)
    booking = booking_repository.find(id)
    user_repository = UserRepository(connection)
    user = user_repository.find(user_id)
    booking_repository.reject(booking)
    send_text_confirmation(booking, user)
    return app.redirect('/requests')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def post_signup():
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    fname = request.form['fname']
    lname = request.form['lname']
    full_name = f"{fname} {lname}"
    email = request.form['email']
    phone_number = request.form['phone_number']
    password = request.form['password']
    password2 = request.form['password2']
    if password != password2:
        flash("Passwords don't match")
        return redirect('/signup')
    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"
    password_regex = re.compile(password_pattern)
    if not re.fullmatch(password_regex, password):
        flash("Invalid password. Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return redirect('/signup')

    try:
        parsed_number = phonenumbers.parse(phone_number, "GB")
        if not phonenumbers.is_valid_number(parsed_number):
            flash("Invalid phone number")
            return redirect('/signup')
    except phonenumbers.phonenumberutil.NumberParseException:
        flash("Invalid phone number")
        return redirect('/signup')
    try:
        user_repository.find_by_email(email)
        flash("User already exists")
        return redirect('/signup')
    except:
        new_user = User(None, full_name, email, password, phone_number)
        new_user = user_repository.create(new_user)
        session['user_id'] = new_user.id
        session['user_email'] = new_user.email
        if request.method == 'POST':
            msg = Message(subject='Welcome to MakersBnB!', sender='makers.bnb@outlook.com', recipients=[email])
            msg.body = f"""Dear {full_name},

Thank you for signing up for MakersBnB! We're thrilled to have you as a member of our community.

At MakersBnB, we strive to provide you with a seamless and enjoyable experience in finding your perfect rental property. Here are a few things you can do to get started:

1. Browse listings: Explore our extensive collection of rental properties from around the world. You can filter and search based on your preferences to find the perfect match. [Insert link to listings page]
2. Contact hosts: If you find a property you're interested in, you can easily get in touch with the host to inquire about availability and ask any questions you may have. [Insert link to contact form or host profiles]
3. Book your rental: Once you've found the ideal property, you can proceed with the booking process. Our platform ensures a seamless experience, allowing you to secure your rental with ease.

We're here to assist you throughout your rental journey. If you have any questions or need assistance, please don't hesitate to reach out to our support team at makers.bnb@outlook.com
Thank you once again for joining MakersBnB. We hope you find your dream rental and have a fantastic experience.

Best regards, 
The MakersBnB Team
"""
            mail.send(msg)


        return app.redirect('/')
        #if user doesnt exists, create into database and redirect home
    

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form['password']
    user_repository = UserRepository(connection)
    try:
        user = user_repository.find_by_email(email)
        print(user.password)
        print(password)
        if user.password == password:
            print(1)
            session['user_id'] = user.id
            print(2)
            session['user_email'] = user.email
            return app.redirect('/spaces')
        #if password matches log them in
        else:
            return render_template('login.html', error="Password incorrect")
        #if user exists in database but passwords don't match then present error message
    except:
        return render_template('login.html', error="Email doesn't exist")
        #if user doesn't exists in database present error message
    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    session.pop('user_email', None)
    return redirect('/login')

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
