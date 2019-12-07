from bson.json_util import dumps
from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo

from flask_cors import CORS
import AuthenticationService
#from AuthenticationService.py import AuthenticationService as auth

# from flask_cors import CORS
# from AuthenticationService.py import AuthenticationService as auth


app = Flask(__name__)
# CORS(app)
app.config["MONGO_URI"] = "mongodb://localhost:27017/anyout"
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
    Username = request.form['Username']
    Email = request.form['Email']

    Password = request.form['Password']


    user_id = users.insert({
        'Username' : Username,
        'Email' : Email,
        'Password':Password,

        })

    new_user = users.find_one({'_id': user_id})
    result = {'Email':new_user['Email']+'registered'}




    
    return "Sign Up successful!"





@app.route('/Events/CreateEvent', methods=['GET','POST'])
#@login_required
def new_event():
    events= mongo.db.events
    title = request.form['title']
    address = request.form['address']
    description = request.form['description']
    capacity = request.form['capacity']

    event_id = events.insert({'title':title,
                             'address':address,
                             'description':description,
                             'capacity':capacity,
                            })

    return "Event Created"
    
    
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
