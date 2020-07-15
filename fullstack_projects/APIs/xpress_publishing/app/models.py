from app import db


class Artist(db.model): #update the logic
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    artist_name = Column(String(250), nullable= False)
    date_of_birth = Column(String(10), nullable=False)
    biography = Column(String(500), nullable=False)
    is_currently_employed = Column(Integer, default = 1)
    issues = db.relationship('Issue', backref='artist')

    def __init__(self, name):
        """initialize with name."""
        self.name = name

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
        return "<Artist: {}>".format(self.name)

class Series(db.model): #update the remaining portion
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    series_name = Column(String(250), nullable=False)
    description = Column(String(500), nullable=False)
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
    id = Column(Integer, primary_key=True)
    issue_name = Column(String(250), nullable = False)
    issue_number = Column(Integer, nullable = False)
    publication_date = Column(String(10), nullable = False)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable = False)
    series_id = Column(Integer, ForeignKey('series.id'), nullable = False)

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
