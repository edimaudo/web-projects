from app import db

class Category(db.model):
	__tablename__ = 'category'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45), default='')

class Customer(db.model):
	__tablename__ = 'customer'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45),nullable=False)
	email = db.Column(db.String(45),nullable=False)
	phone = db.Column(db.String(45),nullable=False)
	address = db.Column(db.String(45),nullable=False)
	city_region = db.Column(db.String(2),nullable=False)
	cc_number = db.Column(db.String(19),nullable=False)

class Product(db.Model):
	__tablename__ = 'product'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45),nullable=False)
	price = db.Column(db.float, nullable=False)
	description = db.Column(db.String(255),nullable=False)
	last_update = db.Column(db.DateTime, default=datetime.utcnow)
	category_id = db.Column(Integer, ForeignKey('category.id'))

class CustomerOrder(db.Model):
	__tablename__ = 'customer_order'
	id = db.Column(db.Integer, primary_key=True)
	amount = db.Column(db.float, nullable=False)
	date_created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
	confirmation_number = db.Column(db.Integer, nullable=False)
	customer_id = db.Column(Integer, ForeignKey('customer.id'))

class OrderedProduct(db.Model):
	__tablename__ = "ordered_product"
	id = db.Column(db.Integer, primary_key=True)
	ordered_product_id  = db.Column(db.Integer, primary_key=True)
	quantity = db.Column(db.Integer, nullable=False)
	customer_order_id = db.Column(Integer, ForeignKey('customer_order.id'))
	product_id = db.Column(Integer, ForeignKey('product.id'))




