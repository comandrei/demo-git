from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Salut din Python "

@app.route("/contact")
def contact():
    return "Pagina de contact"

@app.route("/help")
def help():
    return "Ajutor"


times = 0


@app.route("/visit")
def visit():
    global times
    times += 1
    return f"Visited {times}"



app.run("0.0.0.0")