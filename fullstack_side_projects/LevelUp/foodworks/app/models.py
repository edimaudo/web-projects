from app import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    price = db.Column(db.Float)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(120))
    stock = db.Column(db.Float)

    def __init__(self, title, price, description, image_url, stock): 
    	self.title = title
    	self.price = price
    	self.description = description
    	self.image_url = image_url
    	self.stock = stock