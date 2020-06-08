from app import app
from flask import render_template, flash, redirect, url_for, request
from app.models import Product
@app.route('/')
@app.route('/index')
def index():
	all_data = Product.query.all()
	return render_template('index.html', products = all_data)

@app.route('/add_product', methods=["GET", "POST"])
def add_product():
	if request.method == 'POST':
		title = request.form['title']
		price = request.form['price']
		description = request.form['description']
		image_url = request.form['image_url']
		#stock = request.form['stock']
		my_data = Product(title, price, description, image_url) #add stock later
		db.session.add(my_data)
		db.session.commit()
		flash("Product Added succesfully")
	return redirect(url_for('index'))



@app.route('/view_product')
def view_product():
	return render_template("view_product.html")

@app.route('/edit_product')
def edit_product():
	return render_template("edit_product.html")