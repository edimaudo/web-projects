from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

from flask_sqlalchemy import SQLAlchemy #orm
import os

#added db
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "bookdatabase.db"))

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = database_file

db = SQLAlchemy(app)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_firstname = db.Column(db.String(64), unique=False)
    contact_lastname = db.Column(db.String(64), unique=False)
    contact_email = db.Column(db.String(120), unique=False)

    def __repr__(self):
        return '<Contact {}>'.format(self.contact_firstname, self.contact_lastname, self.contact_email)
        #return '<Contact {}>'.format(self.contact_firstname)


@app.route("/", methods=["GET", "POST"])
def index():
	contacts = None
	if request.form:
		try:
			contact = Contact(contact_firstname=request.form.get("firstname"), contact_lastname=request.form.get("lastname"),
				contact_email=request.form.get("email"))
			db.session.add(contact)
			db.session.commit()
		except Exception as e:
			print("Failed to add Contact")
			print(e)
	contacts = Contact.query.all()
	return render_template("index.html", contacts=contacts)

@app.route("/update", methods=["POST"])
def update():
	try:
		oldfirstname = request.form.get("oldfirstname")
		oldlastname = request.form.get("oldlastname")
		oldemail = request.form.get("oldemail")
		newfirstname = request.form.get("newfirstname")
		newlastname = request.form.get("newlastname")
		newemail = request.form.get("newemail")
		contact = Contact.query.filter_by(contact_firstname=oldfirstname).first()
		contact.contact_firstname = newfirstname
		contact.contact_lastname = newlastname
		contact.contact_email = newemail
		db.session.commit()
	except Exception as e:
		print("Failed to update book")
		print(e)
	return redirect("/")

@app.route("/delete", methods=["POST"])
def delete():
	try:
		cid = request.form.get("contact_id")
		contact = Contact.query.filter_by(id = cid).first()
		db.session.delete(contact)
		db.session.commit()
	except Exception as e:
		print("Failed to delete book")
		print(e)
	return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
