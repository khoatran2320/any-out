from bson.json_util import dumps
from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo

from flask_cors import CORS

import AuthenticationService
#from AuthenticationService.py import AuthenticationService as auth

# from flask_cors import CORS
# from AuthenticationService.py import AuthenticationService as auth


app = Flask(__name__)

app.config["MONGO_URI"] = "mongodb://localhost:27017/anyout"
app.config['SECRET_KEY'] = 'secret'
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app, resources={r"*": {"origins": "http://localhost:8080"}})

mongo = PyMongo(app)
db = mongo.db


@app.route("/", methods=["GET"])
def home():
    return dumps(mongo.db.users.find())


# @app.route("/login", methods=["GET", "POST"])
# # login harry, compare credentials to database
# @app.route("/signup", methods=["GET", "POST"])
# # sign abdel save credentials to database, hash password

@app.route('/register', methods=['POST'])
def register():
    users = mongo.db.users

    # user_id =
    users.insert_one({
        'username': request.form['username'],
        'email': request.form['email'],
        'password': request.form['password'],

    })

    # new_user = users.find_one({'_id': user_id})
    # result = {'Email': new_user['Email']+'registered'}

    return "Sign Up successful!"


@app.route('/createEvent', methods=['POST'])
# @login_required
def new_event():
    events = mongo.db.events
    title = request.form['title']
    address = request.form['address']
    lat = request.form['lat']
    lng = request.form['lng']
    description = request.form['description']
    startTime = request.form['startTime']
    endTime = request.form['endTime']
    capacity = request.form['capacity']

    events.insert_one({'title': title, 'description': description, 'address': address, 'lat': lat,
                       'lng': lng, 'startTime': startTime, 'endTime': endTime, 'capacity': capacity, })

    return "Event Created"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
