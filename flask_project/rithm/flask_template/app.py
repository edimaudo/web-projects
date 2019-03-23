from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/person/<person>/<int:age>')
def say_name_age(person,age):
	return render_template("person.html",person=person,age=age)

@app.route('/calculate')
def calculate():
	return render_template("calc.html")

@app.route('/math')
def print_name():
    number1 = int(request.args.get('Number1'))
    number2 = int(request.args.get('Number2'))
    #selectedOption = "Add"
    selectedOption = str(request.args.get('comp_select'))
    print(selectedOption)
    divideOption = "NaN"
    if selectedOption == "Divide":
    	if number2 != 0:
    		return f"The division of {number1} and {number2} is {number1/number2}."
    	return f"The division of {number1} and {number2} is {divideOption}."
    elif selectedOption == "Multiply":
    	return f"The multiplication of {number1} and {number2} is {number1 * number2}."
    elif selectedOption == "Add":
    	return f"The Addition of {number1} and {number2} is {number1 + number2}."
    elif selectedOption == "Subtract":
    	return f"The subtraction of {number1} and {number2} is {number1 - number2}."
    return "None"