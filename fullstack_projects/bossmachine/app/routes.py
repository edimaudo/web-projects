from app import app
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app import db
from app.errors import errors
from app.models import Minion, Idea, Meeting, Work
#from app.api.errors import error_response as api_error_response

#error handlers
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html')

# @app_errorhandler(500)
# def internal_error(error):
# #     db.session.rollback()
# #     return api_error_response(500)


#key functions
def isMillionDollarIdea(weeklyRevenue, numWeeks):
    totalMoney = numWeeks * weeklyRevenue
    if totalMoney < 1000000:
        return True
    return False


#home
@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html")

/api/minions
GET /api/minions to get an array of all minions.
POST /api/minions to create a new minion and save it to the database.
GET /api/minions/:minionId to get a single minion by id.
PUT /api/minions/:minionId to update a single minion by id.
DELETE /api/minions/:minionId to delete a single minion by id.

	all_data = Product.query.all()
	return render_template('index.html', products = all_data)
#minions
@app.route('/minions')
def minions():
    return render_template("minion.html", all_data = minions)


#ideas
@app.route('/ideas')
def ideas():
    return ""

#meetings
@app.route("meetings")
def meetings():
    return ""

#works


getAllFromDatabase:

Takes only the single argument for model name. Returns the array of elements in the database or null if an invalid argument is supplied
getFromDatabaseById:

Takes the model name argument and a second string argument representing the unique ID of the element. Returns the instance with valid inputs and -1 with an invalid id.
addToDatabase:

Takes the model name argument and a second argument which is an object with the key-value pairs of the new instance. addToDatabase handles assigning .id properties to the instances. It does not check to make sure that valid inputs are supplied, so you will have to add those checks to your routes if necessary. addToDatabase will return the newly-created instance from the database. This function will validate the schema of the instance to create and throw an error if it is invalid.
updateInstanceInDatabase:

Takes the model name argument and a second argument which is an object representing an updated instance. The instance provided must have a valid .id property which will be used to match. updateInstanceInDatabase will return the updated instance in the database or null with invalid inputs. This function will validate the schema of the updated instance and throw an error if it is invalid.
deleteFromDatabasebyId:

Takes the model name argument and a second string argument representing the unique ID of the element to delete. Returns true if the delete occurs properly and false if the element is not found.
deleteAllFromDatabase:

Takes only the single argument for model name. Deletes all elements from the proper model and returns a new, empty array. You will only need to use this function for a /api/meetings route.




/api/ideas
GET /api/ideas to get an array of all ideas.
POST /api/ideas to create a new idea and save it to the database.
GET /api/ideas/:ideaId to get a single idea by id.
PUT /api/ideas/:ideaId to update a single idea by id.
DELETE /api/ideas/:ideaId to delete a single idea by id.

/api/meetings
GET /api/meetings to get an array of all meetings.
POST /api/meetings to create a new meeting and save it to the database.
DELETE /api/meetings to delete all meetings from the database.


GET /api/minions/:minionId/work to get an array of all work for the specified minon.
POST /api/minions/:minionId/work to create a new work object and save it to the database.
PUT /api/minions/:minionId/work/:workId to update a single work by id.
DELETE /api/minions/:minionId/work/:workId to delete a single work by id.



from app import app
from flask import render_template, flash, redirect, url_for, request
from app import db
from app.models import Product


@app.route('/')
@app.route('/index')
def index():
	all_data = Product.query.all()
	return render_template('index.html', products = all_data)

@app.route('/view/<int:id>')
def view_product(id):
	my_data = Product.query.get(id)
	return render_template("view_product.html", product = my_data)

@app.route('/add/', methods=["GET", "POST"])
def add_product():
	if request.method == "POST":
		title = request.form['title']
		price = request.form['price']
		description = request.form['description']
		image_url = request.form['image_url']
		stock = request.form['stock']
		my_data = Product(title, price, description, image_url, stock)
		db.session.add(my_data)
		db.session.commit()
		flash("Product Added succesfully")
		return redirect(url_for('index'))
	return render_template('add_product.html')


@app.route('/update/<int:id>',methods = ['GET', 'POST'])
def update_product(id):
	if request.method == "POST":
		my_data = Product.query.get(id)
		my_data.title = request.form['title']
		my_data.price = request.form['price']
		my_data.description = request.form['description']
		my_data.image_url = request.form['image_url']
		my_data.stock = request.form['stock']
		db.session.commit()
		flash("Product updated succesfully")
		return redirect(url_for("index"))
	else:
		product = Product.query.get(id)
		return render_template("update_product.html", product = product)


@app.route("/delete/<int:id>")
def delete_product(id):
	my_data = Product.query.get(id)
	db.session.delete(my_data)
	db.session.commit()
	flash("Product Deleted succesfully")
	return redirect(url_for("index"))





