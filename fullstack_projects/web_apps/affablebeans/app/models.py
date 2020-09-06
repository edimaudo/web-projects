from app import db

#Cateogory
class Category(db.model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45), default='')

class Customer(db.model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45),nullable=False)
	email = db.Column(db.String(45),nullable=False)
	phone = db.Column(db.String(45),nullable=False)
	address = db.Column(db.String(45),nullable=False)
	city_region = db.Column(db.String(2),nullable=False)
	cc_number = db.Column(db.String(19),nullable=False)



3)customer 
column	Datatype	NN (Not Null)
name	VARCHAR(45)	✓
email	VARCHAR(45)	✓
phone	VARCHAR(45)	✓
address	VARCHAR(45)	✓
city_region	VARCHAR(2)	✓
cc_number	VARCHAR(19)	✓

#Products 

1)product
column	Datatype	PK	NN	UN	AI	Default
id	    INT	 ✓	✓	✓	✓	 
name	VARCHAR(45)	 	✓	 	 	 
price	DECIMAL(5,2)	 	✓	 	 	 
description	TINYTEXT	 	 	 	 	 
last_update	TIMESTAMP	 	✓	 	 	CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
category_id fk taken from category

class Product(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45),nullable=False)
	price
	description
	last_update
	category_id












4)customer_order
Column	Datatype	PK	NN	UN	AI	Default
id	INT	✓	✓	✓	✓	 
amount	DECIMAL(6,2)	 	✓	 	 	 
date_created	TIMESTAMP	 	✓	 	 	CURRENT_TIMESTAMP
confirmation_number	INT	 	✓	✓	 	 
customer_id fk - taken from customer table


5) ordered_product
customer_order_id int
product_id int
quantity smallint
---
fk ordered_product_customer_order_id
fk_ordered_product_product_id



	class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

#one to many
 class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    addresses = db.relationship('Address', backref='person', lazy=True)

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'),
        nullable=False)

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255),default='')
    img_filename = db.Column(db.String(255),default='')
    img_caption = db.Column(db.String(255),default='')
    category = db.Column(db.String(255),default='')

#many to many
tags = db.Table('tags',
    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'), primary_key=True),
    db.Column('page_id', db.Integer, db.ForeignKey('page.id'), primary_key=True)
)

class Page(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
        backref=db.backref('pages', lazy=True))

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)