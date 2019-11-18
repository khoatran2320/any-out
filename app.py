

from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")
@app.route("/login", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
