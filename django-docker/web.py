from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Salut din Python"

app.run("0.0.0.0")