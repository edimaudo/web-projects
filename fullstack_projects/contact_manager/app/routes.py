from app import app
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
	all_data = Product.query.all()
	return render_template('index.html', contacts = all_data)

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

