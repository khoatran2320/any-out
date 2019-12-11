
from bson.json_util import dumps
from flask import Flask, render_template, request, jsonify, Response, session
from flask_pymongo import PyMongo

from flask_cors import CORS

import hashlib


def hashPassword(password):
    salt = "tyuhjhjklnm"
    saltedPassword = password + salt
    hasher = hashlib.sha256(saltedPassword.encode())
    hashedPassword = hasher.hexdigest()
    return hashedPassword


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


@app.route("/login", methods=['POST'])
def login():
    user = mongo.db.users.find_one({'email': request.form['email']})
    print(hashPassword(request.form['password']))
    if user:
        if user['password'] == hashPassword(request.form['password']):
            response = {"key": "SID", "value": user['id']}
            return response
        return Response(status=400)
    return Response(status=400)


# @app.route("/get-events", methods=['GET'])
# def getEvents():
#     cursors = mongo.db.events.find()
#     return_response = {}
#     for event in cursors:


@app.route('/register', methods=['POST'])
def register():
    users = mongo.db.users
    email = users.find_one({'email': request.form['email']})
    if email:
        return Response(status=400)
    else:
        users.insert_one({
            'id': hashPassword(request.form['email']),
            'name': request.form['name'],
            'email': request.form['email'],
            'password': hashPassword(request.form['password']),

        })
        return Response(status=200)


@app.route('/createEvent', methods=['POST'])
# @login_required
def new_event():
    events = mongo.db.events
    id = hashPassword(
        request.form['title']+request.form['description'] + request.form['address'])
    email = events.find_one({'id': id})
    if email:
        return Response(status=400)
    host = request.form['SID']
    title = request.form['title']
    address = request.form['address']
    lat = request.form['lat']
    lng = request.form['lng']
    description = request.form['description']
    startTime = request.form['startTime']
    endTime = request.form['endTime']
    capacity = request.form['capacity']

    events.insert_one({'id': id, 'title': title, 'description': description, 'address': address, 'lat': lat,
                       'lng': lng, 'startTime': startTime, 'endTime': endTime, 'capacity': capacity, 'host': host})

    return Response(status=200)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
