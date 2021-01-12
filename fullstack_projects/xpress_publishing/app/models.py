from app import db
from datetime import datetime

class Artist(db.Model):
    __tablename__ = 'artists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    date_of_birth = db.Column(db.DateTime, nullable = False)
    biography = db.Column(db.Text, nullable = False)
    #grade = db.Column("grade", ENUM("A", "B", "C", "D", "F", name="grade_enum",create_type=False))
    #is_currently_employed = db.Column("is_currently_employed", ENUM("A", "B", "C", "D", "F", name="grade_enum",create_type=False))
    is_currently_employed = db.Column(db.Enum('N','Y'), nullable=False, server_default="N")
    issues = db.relationship('issues', backref='artists', lazy=True)


    def __init__(self, name, date_of_birth, biography, is_currently_employed):
        self.name= name
        self.date_of_birth = date_of_birth
        self.biography = biography
        self.is_currently_employed = is_currently_employed
    
    def __repr__(self):
        return 'Artist {}>'.format(self.name) 

class Series(db.Model):
    __tablename__ = "series"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable = False)
    issues = db.relationship('issues', backref='series', lazy=True)

    def __init__(self, name, description):
        self.name= name
        self.description = description

    def __repr__(self):
        return 'Series {}>'.format(self.name) 

class Issue(db.Model):
    __tablename__ = "issues"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable = False)
    issue_number = db.Column(db.Text, nullable = False)
    publication_date = db.Column(db.DateTime, nullable = False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'),nullable=False)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'),nullable=False)

    def __init__(self, name, issue_number, publication_date):
        self.name= name
        self.issue_number = issue_number
        self.publication_date = publication_date

    def __repr__(self):
        return 'Issues {}>'.format(self.name) 

   
