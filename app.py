import os
from flask import Flask, request, render_template, session, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
from lib.user_repository import UserRepository
from lib.user import User
from lib.space_repository import SpaceRepository
from lib.space import Space

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
        connection = get_flask_database_connection(app)
        user_repository = UserRepository(connection)
        user = user_repository.find(user_id)
        return render_template('index.html', user=user)
    else:
        return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/spaces/new')
def spaces():
    return render_template('list.html')

@app.route('/requests')
def requests():
    user_id = session.get('user_id')
    connection = get_flask_database_connection(app)
    user_repository = UserRepository(connection)
    user = user_repository.find(user_id)
    return render_template('requests.html', user=user)

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

    return render_template('list.html')



@app.route('/signup', methods=['POST'])
def post_signup():
    connection = get_flask_database_connection(app)
    email = request.form['email'] 
    fname = request.form['fname'] 
    lname = request.form['lname'] 
    full_name = f"{fname} {lname}"
    password = request.form['password']
    phone_number = request.form['phone_number'] 

    
    user_repository = UserRepository(connection)
    new_user = User(None, full_name, email, password, phone_number)
    try: 
        user_repository.find_by_email(email)
        return render_template('signup.html', error="User already exists")
        #if user exists return back to signup page with error message
    except:
        user_repository.create(new_user)
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
    user = user_repository.find_by_email(email)
    
    if user and user.password == password:
        session['user_id'] = user.id
        return redirect('/')
    else:
        return render_template('login.html', error="Invalid email or password")
    
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect('/')




# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
