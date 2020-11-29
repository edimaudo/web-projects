from app import db

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120))
    last_name = db.Column(db.String(120))
    phone_number = db.Column(db.String(120))
    email = db.Column(db.String(120))
    note= db.Column(db.String(255))


    def __repr__(self):
        return '<Contact {}>'.format(self.title) 

    def __init__(self, first_name, last_name, phone_number, email, note): 
    	self.first_name = first_name
    	self.last_name = last_name
    	self.phone_number = phone_number
    	self.email = email
    	self.note = note



