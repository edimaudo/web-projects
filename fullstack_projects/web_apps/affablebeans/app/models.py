from app import db
import datetime as datetime

class Category(db.Model):
	__tablename__ = 'category'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45), default='')

	def __repr__(self):
		return '<Category {}>'.format(self.name)

	def __init__(self, name):
		self.name = name

class Customer(db.Model):
	__tablename__ = 'customer'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45),nullable=False)
	email = db.Column(db.String(45),nullable=False)
	phone = db.Column(db.String(45),nullable=False)
	address = db.Column(db.String(45),nullable=False)
	city_region = db.Column(db.String(2),nullable=False)
	cc_number = db.Column(db.String(19),nullable=False)

	def __repr__(self):
		return '<Customer {}>'.format(self.name)

	def __init__(self, name, email, phone, address, city_region, cc_number):
		self.name = name
		self.email = email
		self.phone = phone
		self.address = address
		self.city_region = city_region
		self.cc_number = cc_number

class Product(db.Model):
	__tablename__ = 'product'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45),nullable=False)
	price = db.Column(db.Float, nullable=False)
	description = db.Column(db.String(255),nullable=False)
	last_update = db.Column(db.DateTime, default=datetime.datetime)
	category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

	def __repr__(self):
		return '<Product {}>'.format(self.name)

	def __init__(self, name, price, description, last_update, category_id):
		self.name = name
		self.price = price
		self.description= description
		self.last_update = last_update
		self.category_id = category_id

class CustomerOrder(db.Model):
	__tablename__ = 'customer_order'
	id = db.Column(db.Integer, primary_key=True)
	amount = db.Column(db.Float, nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.datetime, nullable=False)
	confirmation_number = db.Column(db.Integer, nullable=False)
	customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'))

	def __repr__(self):
		return '<CustomerOrder {}>'.format(self.id)

	def __init__(self, amount, date_created, confirmation_number, customer_id):
		self.amount = amount
		self.date_created = date_created
		self.confirmation_number = confirmation_number
		self.customer_id = customer_id


class OrderedProduct(db.Model):
	__tablename__ = "ordered_product"
	id = db.Column(db.Integer, primary_key=True)
	ordered_product_id  = db.Column(db.Integer, primary_key=True)
	quantity = db.Column(db.Integer, nullable=False)
	customer_order_id = db.Column(db.Integer, db.ForeignKey('customer_order.id'))
	product_id = db.Column(db.Integer, db.ForeignKey('product.id'))
	
	def __repr__(self):
		return '<Ordered {}>'.format(self.id)

	def __init__(self, ordered_product_id, quantity, customer_order_id, product_id):
		self.ordered_product_id = ordered_product_id
		self.quantity = quantity
		self.customer_order_id
		self.product_id




