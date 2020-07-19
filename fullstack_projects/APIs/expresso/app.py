from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Employee, Timesheet, Menu, MenuItem

# Connect to Database and create database session
engine = create_engine('sqlite:///expresso.db?check_same_thread=False')
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
@app.route('/employeesApi/<int:employee_id>', methods=['GET', 'PUT', 'DELETE'])
def employee_api_id(employee_id):
    if request.method == 'GET':
        return employee(employee_id)
    elif request.method == 'PUT':
        employee_name = request.args.get('employee_name', '')
        position = request.args.get('position', '')
        wage = request.args.get('wage', '')
        is_currently_employee = request.args.get('is_currently_employee','')
    	return update_employee(employee_id, employee_name, position, wage, is_currently_employee)
    elif request.method == 'DELETE':
    	return delete_employee(id)

#==========
#/api/employees/:employeeId/timesheets
#==========
@app.route('/employeesApi/<int:employee_id>/timesheets', methods=['GET', 'POST'])
def employee_api_timesheet(employee_id):
	if request.method == "GET":
		return employees_timesheet(employee_id)
	elif request.method == 'POST':
		hours = request.args.get('hours','')
		rate = request.args.get('rate','')
		date = request.args.get('date','')
		return create_timesheet(employee_id, hours, rate, date)

#==========
#/api/employees/:employeeId/timesheets/:timesheetId
#==========
@app.route('/employeesApi/<int:employee_id>/timesheets/<int:timesheet_id>', 
	methods=['GET', 'PUT', 'DELETE'])
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
@app.route('/menusApi/<int:menu_id>', methods=['GET', 'PUT', 'DELETE'])
def menu_api_id(menu_id):
	if request.method == 'GET':
		return menu(menu_id)
	elif request.method == 'PUT':
		title = request.args.get('title','')
		return update_menu(menu_id, title)
	elif request.method == 'DELETE':
		return delete_menu(menu_id)

#==========
# /api/menus/:menuId/menu-items
#==========
@app.route('/menusApi/<int:menu_id>/menu-items', methods=['GET', 'POST'])
def menu_api_menu_items(menu_id):
	if request.method == 'GET':
		return menu_items(menu_id)
	elif request.method == 'POST':
		menu_item_name = request.args.get('menu_item_name','')
		description = request.args.get('description','')
		inventory = request.args.get('inventory','')
		price = request.args.get('price','')
		return create_menu_item(menu_id, menu_item_name, description, inventory, price)

#==========
# /api/menus/:menuId/menu-items/:menuItemId
#==========
@app.route('/menusApi/<int:menu_id>/menu-items/<int:menu_item_id>', methods=['PUT', 'DELETE'])
def menu_api_menu_item_id(menu_id, menu_item_id):
	if request.method == 'PUT':
		menu_item_name = request.args.get('menu_item_name','')
		description = request.args.get('description','')
		inventory = request.args.get('inventory','')
		price = request.args.get('price','')
		return update_menu_menu_item(menu_id, menu_item_id, menu_item_name, 
			description, inventory, price)
	elif request.method == 'DELETE':
		return delete_menu_item(menu_id, menu_item_id)

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)