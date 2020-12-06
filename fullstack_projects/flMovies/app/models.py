from app import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    genre = db.Column(db.String(50))
    release_date = db.Column(db.String(50))
    price = db.Column(db.Float)

    def __repr__(self):
        return '<Movie {}>'.format(self.title) 

    def __init__(self, title, genre, release_date, price): 
    	self.title = title
    	self.genre = genre
    	self.release_date = release_date
    	self.price = price