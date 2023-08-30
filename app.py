import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
from lib.user_repository import UserRepository
from lib.user import User

# Create a new Flask app
app = Flask(__name__)

@app.route('/spaces', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('spaces.html', spaces=spaces )

@app.route('/spaces/<id>', methods=['GET'])
def get_index_redirect(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template('space.html', space=space)

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
    try:
        user = user_repository.find_by_email(email)
        if user.password == password:
            return render_template('index.html', user=user)
        #if password matches log them in
        else:
            return render_template('login.html', error="Password incorrect")
        #if user exists in database but passwords don't match then present error message
    except:
        return render_template('login.html', error="Email doesn't exist")
        #if user doesn't exists in database present error message



# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
