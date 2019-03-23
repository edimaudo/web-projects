# Build a simple calculator! You should have routes that can perform addition, subtraction, 
#multiplication and division with two numbers so if a request is made to /add/2/2 
#the server should respond with 4.

# Bonus
# Refactor your code so that all of these operations can be done in a single route called /math

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome!"


@app.route('/math/<int:num>/<int:num1>')
def math(num,num1):
	division_output = "NaN"
	if num1 != 0:
		division_output = num/num1 

	return f"The addition of {num} and {num1} is {num + num1}." + \
	f"  The subtraction of {num} and {num1} is {num - num1}." + \
	f"  The multiplication of {num} and {num1} is {num * num1}." + \
	f"  The division of {num} and {num1} is {division_output}."





