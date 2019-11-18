
from mongoengine import connect
from flask import Flask, render_template, request
db = connect('anyout')

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    
    return render_template("home.html")
# @app.route("/login", methods=["GET", "POST"])

# @app.route("/signup", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
