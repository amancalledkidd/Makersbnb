import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.space import *
from lib.space_repository import *
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/', methods=['GET'])
def get_index():
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    spaces = repository.all()
    return render_template('index.html', spaces=spaces )

@app.route('/listing/<id>', methods=['GET'])
def get_index_redirect(id):
    connection = get_flask_database_connection(app)
    repository = SpaceRepository(connection)
    space = repository.find(id)
    return render_template('listing.html', space=space)
# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
