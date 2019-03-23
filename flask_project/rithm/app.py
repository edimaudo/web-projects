from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def welcome():
    names_of_instructors = ["Elie", "Tim", "Matt"]
    random_name = "Tom"
    return render_template('index.html', names=names_of_instructors, name=random_name)

@app.route('/title')
def title():
    return render_template('title.html')

@app.route('/second')
def second():
    return "WELCOME TO THE SECOND PAGE!"




