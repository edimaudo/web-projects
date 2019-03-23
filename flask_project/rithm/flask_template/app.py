from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/person/<person>/<int:age>')
def say_name_age(person,age):
	return render_template("person.html",person=person,age=age)

@app.route('/calculate')
def calculate():
	return render_template("calc.html")