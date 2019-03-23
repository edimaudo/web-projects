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

# we need a route to render the form
@app.route('/show-form')
def show_form():
    return render_template('first-form.html')

# we need to do something when the form is submitted
@app.route('/data')
def print_name():
    first = request.args.get('first')
    last = request.args.get('last')
    return f"You put {first} {last}"




