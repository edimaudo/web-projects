from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Artist, Series, Issue

# Connect to Database and create database session
engine = create_engine('sqlite:///xpress_publishing.db?check_same_thread=False')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

#============
#html routes
#===========


#===========
# helper functions - should
#===========

#===========
# /api/employees
#===========
    employee_name = Column(String(250), nullable= False)
    position = Column(String(250), nullable= False)
    wage = Column(Float, nullable = False)
    is_currently_employee = Column(Integer, default = 1)

@app.route('/employeesApi', methods=['GET', 'POST'])
def employeeFunction():
    if request.method == 'GET':
        return get_employees()
    elif request.method == 'POST':
        employee_name = request.args.get('employee_name', '')
        position = request.args.get('position', '')
        wage = request.args.get('wage', '')
        is_currently_employee = request.args.get('is_currently_employee','')
        return makeANewEmployee(employee_name, position, wage, is_currently_employee)

#===========
# /api/employees/:employeeId
#===========
@app.route('/employeesApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def employeeFunctionId(id):
    if request.method == 'GET':
        return get_employees(id)
    elif request.method == 'PUT':
        employee_name = request.args.get('employee_name', '')
        position = request.args.get('position', '')
        wage = request.args.get('wage', '')
        is_currently_employee = request.args.get('is_currently_employee','')
    	return updateEmployee(id, employee_name, position, wage, is_currently_employee)
    elif request.method == 'DELETE':
    	return deleteArtist(id)


@app.route('/employeesApi/<int:id>/timesheets', methods=['GET', 'POST'])
def employeeTimesheetFunction(id):
	if request.method == "GET":
		return get_employees_timesheet(id)
	elif request.method == 'POST':
		hours = request.args.get('hours','')
		rate = request.args.get('rate','')
		date = request.args.get('date','')
		return makeNewTimesheet(id, hours, rate, date)


@app.route('/employeesApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])

# /api/employees/:employeeId/timesheets/:timesheetId
# PUT
# Updates the timesheet with the specified timesheet ID using the information from the timesheet property of the request body and saves it to the database. Returns a 200 response with the updated timesheet on the timesheet property of the response body
# If any required fields are missing, returns a 400 response
# If an employee with the supplied employee ID doesn't exist, returns a 404 response
# If an timesheet with the supplied timesheet ID doesn't exist, returns a 404 response
# DELETE
# Deletes the timesheet with the supplied timesheet ID from the database. Returns a 204 response.
# If an employee with the supplied employee ID doesn't exist, returns a 404 response
# If an timesheet with the supplied timesheet ID doesn't exist, returns a 404 response

# /api/menus
# GET
# Returns a 200 response containing all saved menus on the menus property of the response body
# POST
# Creates a new menu with the information from the menu property of the request body and saves it to the database. Returns a 201 response with the newly-created menu on the menu property of the response body
# If any required fields are missing, returns a 400 response

# /api/menus/:menuId
# GET
# Returns a 200 response containing the menu with the supplied menu ID on the menu property of the response body
# If a menu with the supplied menu ID doesn't exist, returns a 404 response
# PUT
# Updates the menu with the specified menu ID using the information from the menu property of the request body and saves it to the database. Returns a 200 response with the updated menu on the menu property of the response body
# If any required fields are missing, returns a 400 response
# If a menu with the supplied menu ID doesn't exist, returns a 404 response
# DELETE
# Deletes the menu with the supplied menu ID from the database if that menu has no related menu items. Returns a 204 response.
# If the menu with the supplied menu ID has related menu items, returns a 400 response.
# If a menu with the supplied menu ID doesn't exist, returns a 404 response

# /api/menus/:menuId/menu-items
# GET
# Returns a 200 response containing all saved menu items related to the menu with the supplied menu ID on the menu items property of the response body
# If a menu with the supplied menu ID doesn't exist, returns a 404 response
# POST
# Creates a new menu item, related to the menu with the supplied menu ID, with the information from the menuItem property of the request body and saves it to the database. Returns a 201 response with the newly-created menu item on the menuItem property of the response body
# If any required fields are missing, returns a 400 response
# If a menu with the supplied menu ID doesn't exist, returns a 404 response

# /api/menus/:menuId/menu-items/:menuItemId
# PUT
# Updates the menu item with the specified menu item ID using the information from the menuItem property of the request body and saves it to the database. Returns a 200 response with the updated menu item on the menuItem property of the response body
# If any required fields are missing, returns a 400 response
# If a menu with the supplied menu ID doesn't exist, returns a 404 response
# If a menu item with the supplied menu item ID doesn't exist, returns a 404 response
# DELETE
# Deletes the menu item with the supplied menu item ID from the database. Returns a 204 response.
# If a menu with the supplied menu ID doesn't exist, returns a 404 response
# If a menu item with the supplied menu item ID doesn't exist, returns a 404 response

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)