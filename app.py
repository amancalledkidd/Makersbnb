import os
from flask import Flask, request, render_template, session, redirect, url_for, flash
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
from lib.user_repository import UserRepository
from lib.user import User
from lib.space_repository import SpaceRepository
from lib.space import Space
from lib.booking_repository import BookingRepository
from lib.booking import Booking
import phonenumbers
import re

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /
# Returns the homepage
app.config['SECRET_KEY'] = 'your_secret_key'

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
    return app.redirect(f'/my_requests')


@app.route('/signup')
def signup():
    return render_template('signup.html')

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
    # start_date = request.form['start_date']
    # end_date = request.form['end_date']
    user_id = request.form['user_id']
    space_repository = SpaceRepository(connection)
    new_space = Space(None, name, address, price, description, user_id)
    space_repository.create(new_space)
    return app.redirect('/spaces')

@app.route('/my_requests')
def requests():
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = user_repository.find_user_with_bookings(user_id)
    return render_template('my_requests.html', user=user)


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
    password_pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,}$"
    password_regex = re.compile(password_pattern)

    if not re.fullmatch(password_regex, password):
        flash("Invalid password. Password must be at least 8 characters long and contain at least one uppercase letter, one lowercase letter, one digit, and one special character.")
        return redirect('/signup')
    if password != password2:
        flash("Passwords don't match")
        return redirect('/signup')

    
    #install pip phonenumber
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
        return redirect('/')

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
        if user.password == password:
            session['user_id'] = user.id
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
    return redirect('/login')



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
