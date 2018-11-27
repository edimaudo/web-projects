from datetime import datetime
from app import db

class Idea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    idea_name = db.Column(db.String(50))
    idea_description = db.Column(db.String(140))

    def __repr__(self):
        return '<Idea {}>'.format(self.idea_name)