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
# helper functions
#===========


#===========
#API functions
#===========

#===========
# /api/employees
#===========

@app.route('/employeesApi', methods=['GET', 'POST'])
def employee_api():
    if request.method == 'GET':
        return employees()
    elif request.method == 'POST':
        employee_name = request.args.get('employee_name', '')
        position = request.args.get('position', '')
        wage = request.args.get('wage', '')
        is_currently_employee = request.args.get('is_currently_employee','')
        return create_employee(employee_name, position, wage, is_currently_employee)

#===========
# /api/employees/:employeeId
#===========
@app.route('/employeesApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def employee_api_id(id):
    if request.method == 'GET':
        return employee(id)
    elif request.method == 'PUT':
        employee_name = request.args.get('employee_name', '')
        position = request.args.get('position', '')
        wage = request.args.get('wage', '')
        is_currently_employee = request.args.get('is_currently_employee','')
    	return update_employee(id, employee_name, position, wage, is_currently_employee)
    elif request.method == 'DELETE':
    	return delete_employee(id)


@app.route('/employeesApi/<int:employee_id>/timesheets', methods=['GET', 'POST'])
def employee_api_timesheet(employee_id):
	if request.method == "GET":
		return employees_timesheet(employee_id)
	elif request.method == 'POST':
		hours = request.args.get('hours','')
		rate = request.args.get('rate','')
		date = request.args.get('date','')
		return create_timesheet(employee_id, hours, rate, date)


@app.route('/employeesApi/<int:employee_id>/timesheets/<int:timesheet_id', methods=['GET', 'PUT', 'DELETE'])
def employee_api_timesheet_id(employee_id,timesheet_id):
	if request.method == 'PUT':
		hours = request.args.get('hours','')
		rate = request.args.get('rate','')
		date = request.args.get('date','')
		return update_employee_timesheet(employee_id,timesheet_id, hours, rate, date)
	elif request.method == 'DELETE':
		return delete_employee_timesheet(employee_id,timesheet_id)


#==========
# /api/menus
#=========
@app.route('/menusApi', methods=['GET', 'POST'])
def menu_api():
	if request.method == "GET":
		return menus()
	elif request.method == 'POST':
		title  = request.args.get('title ','')
		return create_menu(title)

#==========
# /api/menus/:menuId
#==========
@app.route('/menusApi/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def menu_api_id(id):
	if request.method == 'GET':
		return menu(id)
	elif request.method == 'PUT':
		title = request.args.get('title','')
		return update_menu(id, title)
	elif request.method == 'DELETE':
		return delete_menu(id)

#==========
# /api/menus/:menuId/menu-items
#==========
@app.route('/menusApi/<int:id>/menu-items', methods=['GET', 'POST'])

# GET
# Returns a 200 response containing all saved menu items related to the menu with the supplied menu ID on the menu items property of the response body
# If a menu with the supplied menu ID doesn't exist, returns a 404 response
# POST
# Creates a new menu item, related to the menu with the supplied menu ID, with the information from the menuItem property of the request body and saves it to the database. Returns a 201 response with the newly-created menu item on the menuItem property of the response body
# If any required fields are missing, returns a 400 response
# If a menu with the supplied menu ID doesn't exist, returns a 404 response

#==========
# /api/menus/:menuId/menu-items/:menuItemId
#==========
@app.route('/menusApi/<int:menu_id>/menu-items/menu_item_id', methods=['PUT', 'DELETE'])

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