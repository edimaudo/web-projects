from app import db


class Artist(db.model): #update the logic
    __tablename__ = 'artist'
    id = Column(db.Integer, primary_key=True)
    artist_name = Column(db.String(250), nullable= False)
    date_of_birth = Column(db.DateTime, nullable=False)
    biography = Column(db.String(500), nullable=False)
    is_currently_employed = Column(db.Integer, default = 1)
    issues = db.relationship('Issue', backref='artist')

    def __init__(self, artist_name):
        """initialize with name."""
        self.artist_name = artist_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Artist.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Artist: {}>".format(self.artist_name)

class Series(db.model): #update the remaining portion
    __tablename__ = 'series'
    id = Column(db.Integer, primary_key=True)
    series_name = Column(db.String(250), nullable=False)
    description = Column(db.String(500), nullable=False)
    issues = db.relationship('Issue', backref='series')

    def __init__(self, series_name):
        """initialize with name."""
        self.series_name = series_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Series.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Series: {}>".format(self.series_name)



class Issue(db.model): #update remaining part
    __tablename__ = 'issue'
    id = Column(db.Integer, primary_key=True)
    issue_name = Column(db.String(250), nullable = False)
    issue_number = Column(db.Integer, nullable = False)
    publication_date = Column(db.DateTime, nullable = False)
    artist_id = Column(db.Integer, ForeignKey('artist.id'), nullable = False)
    series_id = Column(db.Integer, ForeignKey('series.id'), nullable = False)

    def __init__(self, issue_name):
        """initialize with name."""
        self.issue_name = issue_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Issue.query.all()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "<Issue: {}>".format(self.issue_name)
