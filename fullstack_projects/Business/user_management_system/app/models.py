from app import db

#user model
# class User(db.Model, UserMixin):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)

#     # User Authentication fields
#     email = db.Column(db.String(255), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)


# # Setup Flask-User
#  user_manager = UserManager(app, db, User)

#company model fix
class Company(db.model):
	__tablename__ = 'company'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), default='')
	address = db.Column(db.String(255), default='')
	city = db.Column(db.String(255), default='')
	country = db.Column(db.String(255), default='')
	industry = db.Column(db.String(255), default='')
	languages = db.Column(db.PickleType, nullable=False)
	sectors = db.Column(db.PickleType, nullable=False)
	contacts = db.relationship('Contact', backref='person', lazy=True)

	def __repr__(self):
		return '<Company {}>'.format(self.name)

	def __init__(self,name, address,city, country, industry, languages, sectors):
		self.name = name
		self.address = address
		self.city = city
		self.country = country
		self.industry = industry
		self.languages = languages
		self.sectors = sectors


#contact model
class Contact(db.model):
	__tablename__ = 'contact'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), default='')
	email = db.Column(db.String(255), default='')
	number = db.Column(db.String(255), default='')
	company_id = db.Column(db.Integer, db.ForeignKey('company.id'),nullable=False)

	def __repr__(self):
		return '<Company {}>'.format(self.name)

	def __init__(self, name, email, number):
		self.name = name
		self.email = email
		self.number = number


contactHistory = db.Table('contactHistory',
    db.Column('contact_id', db.Integer, db.ForeignKey('contact.id'), primary_key=True),
    db.Column('company_id', db.Integer, db.ForeignKey('company.id'), primary_key=True)
)

#contact history model
class ContactHistory(db.model):
	#__tablename__ = 'contactHistory'
	id = db.Column(db.Integer, primary_key=True)
	comments = db.Column(db.Text,default='')
	comments_date = db.Column(db.DateTime,nullable = False)


#country
class Country(db.model):
	__tablename__ = 'country'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), default='')

#industry
class Industry(db.model):
	__tablename__ = 'industry'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), default='')
	sectors = db.relationship('Sector', backref='person', lazy=True)

#sector
class Sector(db.model):
	__tablename__ = 'sector'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), default='')
	industry_id = db.Column(db.Integer, db.ForeignKey('industry.id'),nullable=False)

#language
class Language(db.model):
	__tablename__ = 'language'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255), default='')
