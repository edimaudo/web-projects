from app import app
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/add_product')
def add_product():
	return render_template("add_product.html")


@app.route('/view_product')
def view_product():
	return render_template("view_product.html")

@app.route('/edit_product')
def edit_product():
	return render_template("edit_product.html")