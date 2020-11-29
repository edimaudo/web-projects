from app import app
from flask import render_template, flash, redirect, url_for, request
from app import db
from app.models import Contact

@app.route('/')
@app.route('/index')
def index():
	all_data = Contact.query.all()
	return render_template('index.html', contacts = all_data)

@app.route('/view_contact/<int:id>')
def view_contact(id):
	my_data = Contact.query.get(id)
	return render_template("view_contact.html", contact = my_data)

@app.route('/add_contact/', method=['GET','POST'])
def add_contact():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone_number = request.form['phone_number']
        email = request.form['email']
        note = request.form['note']
        my_data = Contact(first_name, last_name, phone_number, email, note)
        db.session.add(my_data)
        db.session.commit()
        flash("Contact Added Sucessfully")
        return redirect(url_for("index"))
    return render_template("add_contact.html")

@app.route('/edit_contact/<int:id>',methods = ['GET', 'POST'])
def update_product(id):
	if request.method == "POST":
		my_data = Contact.query.get(id)
		my_data.first_name = request.form['first_name']
		my_data.last_name= request.form['last_name']
		my_data.phone_number = request.form['phone_number']
		my_data.email = request.form['email']
		my_data.note = request.form['note']
		db.session.commit()
		flash("Product updated succesfully")
		return redirect(url_for("index"))
	else:
		product = Product.query.get(id)
		return render_template("update_product.html", product = product)


@app.route("/delete_product/<int:id>")
def delete_product(id):
	my_data = Product.query.get(id)
	db.session.delete(my_data)
	db.session.commit()
	flash("Product Deleted succesfully")
	return redirect(url_for("index"))

