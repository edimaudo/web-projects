from app import app
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
	all_data = Product.query.all()
	return render_template('index.html', products = all_data)