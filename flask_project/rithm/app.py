from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/name')
def name():
    return "Welcome to our application!"


@app.route('/welcome')
def welcome():
    return "Welome"


@app.route('/welcome/home')
def home():
    return "Welcome home"


@app.route('/welcome/back')
def back():
    return "Welcome back"


@app.route('/sum')
def sum():
    return "ten"