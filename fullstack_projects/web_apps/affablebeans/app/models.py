from app import db

class Category(db.model):
	__tablename__ = 'category'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45), default='')

	def __repr__(self):
        return '<Category {}>'.format(self.name)

	def __init__(self,id, name):
        self.id = id
        self.name = name

class Customer(db.model):
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

	def __init__(self,id, name, email, phone, address, city_region, cc_number):
        self.id = id
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
	price = db.Column(db.float, nullable=False)
	description = db.Column(db.String(255),nullable=False)
	last_update = db.Column(db.DateTime, default=datetime.utcnow)
	category_id = db.Column(Integer, ForeignKey('category.id'))

	def __repr__(self):
        return '<Product {}>'.format(self.name)

	def __init__(self,id, name, price, description, last_update, category_id):
        self.id = id
        self.name = name
        self.price = price
        self.description= description
        self.last_update = last_update
        self.category_id = category_id

class CustomerOrder(db.Model):
	__tablename__ = 'customer_order'
	id = db.Column(db.Integer, primary_key=True)
	amount = db.Column(db.float, nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	confirmation_number = db.Column(db.Integer, nullable=False)
	customer_id = db.Column(Integer, ForeignKey('customer.id'))

	def __repr__(self):
        return '<CustomerOrder {}>'.format(self.id)

	def __init__(self,id, amount, date_created, confirmation_number, customer_id):
        self.id = id
        self.amount = amount
        self.date_created = date_created
        self.confirmation_number = confirmation_number
        self.customer_id = customer_id


class OrderedProduct(db.Model):
	__tablename__ = "ordered_product"
	id = db.Column(db.Integer, primary_key=True)
	ordered_product_id  = db.Column(db.Integer, primary_key=True)
	quantity = db.Column(db.Integer, nullable=False)
	customer_order_id = db.Column(Integer, ForeignKey('customer_order.id'))
	product_id = db.Column(Integer, ForeignKey('product.id'))
	
	def __repr__(self):
        return '<Ordered {}>'.format(self.id)

	def __init__(self,id, ordered_product_id, quantity, customer_order_id, product_id):
        self.id = id
        self.ordered_product_id = ordered_product_id
        self.quantity = quantity
        self.customer_order_id
        self.product_id




