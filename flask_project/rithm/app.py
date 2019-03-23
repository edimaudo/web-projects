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

# #let's make up a parameter called name. Its value is going to be WHATEVER someone requests, but we will respond with the string "The name is" along with the value in the URL.
#@app.route('/name/<person>')
#def say_name(person):
#     return f"The name is {person}"

# # since all URL parameters are strings, we can convert them right away to another data type in our route definition
# @app.route('/name/<int:num>')
# def favorite_number(num):
#     return f"Your favorite number is {num}, which is half of {num * 2}"


# Build a simple calculator! You should have routes that can perform addition, subtraction, 
#multiplication and division with two numbers so if a request is made to /add/2/2 
#the server should respond with 4.

# Bonus
# Refactor your code so that all of these operations can be done in a single route called /math

