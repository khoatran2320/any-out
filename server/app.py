from bson.json_util import dumps
from bson import Binary, Code
from flask import Flask, render_template, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from AuthenticationService.py import AuthenticationService as auth

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

@app.route('/register', methods=['POST'])
def register():
    Username = request.form()['Username']
    Email = request.form()['Email']
    Password = hash_Password(request.get_json()['Password'])


user_id = users.insert({
'Username' :Username,
'Email' :Email,
'Password':Password,
})



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
