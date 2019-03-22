from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/name')
def welcome():
    return "Welcome to our application!"


@app.route('/welcome')
def welcome():
    return "Welome"


@app.route('/welcome/home')
def welcome():
    return "Welcome home"


@app.route('/welcome/back')
def welcome():
    return "Welcome back"


@app.route('/sum')
def welcome():
    return 5 + 5