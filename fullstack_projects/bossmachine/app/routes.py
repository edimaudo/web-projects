from app import app
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app import db
from app.errors import errors
#from app.api.errors import error_response as api_error_response


# @app_errorhandler(404)
# def not_found_error(error):
#     return api_error_response(404)


# @app_errorhandler(401)
# def not_found_error(error):
#     return api_error_response(401)


# @errors.app_errorhandler(500)
# def internal_error(error):
#     db.session.rollback()
#     return api_error_response(500)


#key functions
def isMillionDollarIdea(weeklyRevenue, numWeeks):
    totalMoney = numWeeks * weeklyRevenue
    if totalMoney < 1000000:
        return True
    return False

@app.route('/')
@app.route('/index')
def index():
   return render_template("index.html")


#minions
@app.route('/minions')
def minions():
    return ""


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

/api/minions
GET /api/minions to get an array of all minions.
POST /api/minions to create a new minion and save it to the database.
GET /api/minions/:minionId to get a single minion by id.
PUT /api/minions/:minionId to update a single minion by id.
DELETE /api/minions/:minionId to delete a single minion by id.


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