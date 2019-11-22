from bson.json_util import dumps
from bson import Binary, Code
from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
#from AuthenticationService.py import hash_Password(password)

app = Flask(__name__)
CORS(app)
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

@app.route('/users/register', methods=['POST'])
def register():
users = mongo.db.users
first_name = request.get_json()['first_name']
last_name = request.get_json()['last_name']
email = request.get_json()['email']
password = hash_Password(request.get_json()['password'])


user_id = users.insert({
'first_name' :first_name,
'last_name': last_name,
'email' :email,
'password':password,
})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
