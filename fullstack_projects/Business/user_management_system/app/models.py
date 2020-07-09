from app import db

Company 
- Has a number of fields. Each company is linked to 1 country, multiple languages, 
1 industry, multiple sectors. 
Each company can have 0 to multiple contacts. 
A company can have a direct contact history (in the case of 0 contacts) 
or contact history associated with each contact. 

Contact - Each contact has a number of fields. 
Each contact may be linked to multiple companies, multiple sectors. 
All users can add / edit contacts.  
Each contact can multiple contact histories associated with each company

Contact History - All users can add a contact history entry. 
Only admins and the user who added the entry can edit it. 
Each contact history entry is tied to a contact.  It can also be tied to a company


#company (company name, company address, company city, company country, company industry, 
#company languages, company sectors)

#contact (contact name, contact email, contact number, contact_company)

#contact history (contact name, contact comments, comment date, contact company)

#user model
# Define User data-model
# class User(db.Model, UserMixin):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)

#     # User Authentication fields
#     email = db.Column(db.String(255), nullable=False, unique=True)
#     email_confirmed_at = db.Column(db.DateTime())
#     username = db.Column(db.String(50), nullable=False, unique=True)
#     password = db.Column(db.String(255), nullable=False)

#     # User fields
#     active = db.Column(db.Boolean()),
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)

# # Setup Flask-User
# user_manager = UserManager(app, db, User)

#company model fix
class Company(db.model):
	__tablename__ = 'company'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(255), default='')
	address = db.Column(db.String(255), default='')
	city = db.Column(db.String(255), default='')
	country_id = db.Column(db.Integer, db.ForeignKey('country.id'),nullable=False)
	industry_id = db.Column(db.Integer, db.ForeignKey('industry.id'),nullable=False)
	language_id = db.Column(db.Integer, db.ForeignKey('language.id'),nullable=False)
	sector_id = db.Column(db.Integer, db.ForeignKey('sector.id'),nullable=False)

	def __repr__(self):
		return '<Company {}>'.format(self.name)

	def __init__(self,name, address,city):
		self.name = name
		self.address = address
		self.city = city
		#self.country = country
		#self.industry = industry
		#self.languages = languages
		#self.sectors = sectors


#contact model fix
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


#contact history model


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
