import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /
# Returns the homepage

@app.route('/', methods=['GET'])
def get_index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')



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

    user_repository.create(new_user)
    return app.redirect('/')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def post_login():
    connection = get_flask_database_connection(app)
    email = request.form['email'] 
    password = request.form['password']

    user_repository = UserRepository(connection)

    user = user_repository.check_email_and_password(email, password)
    if user:
        return app.redirect('/')
    else:
        return render_template('login.html', error="Password incorrect")



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
