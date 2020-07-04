import sys

# for creating the mapper code
from sqlalchemy import Column, ForeignKey, Integer, String

# for configuration and class code
from sqlalchemy.ext.declarative import declarative_base

# for creating foreign key relationship between the tables
from sqlalchemy.orm import relationship

# for configuration
from sqlalchemy import create_engine

# create declarative_base instance
Base = declarative_base()

# We will add classes here
class Artist(Base):
    __tablename__ = 'artist'
    id = Column(Integer, primary_key=True)
    artist_name = Column(String(250), nullable= False)
    date_of_birth = Column(DateTime, nullable=False)
    biography = Column(String(500), nullable=False)
    is_currently_employed = Column(Integer, default = 1)

    @property
    def serialize(self):
        return {
            'artist_name': self.artist_name,
            'date_of_birth': self.date_of_birth,
            'biography': self.biography,
            'is_currently_employed': self.is_currently_employed,
            'id':self.id,
        }

class Series(Base):
    __tablename__ = 'series'
    id = Column(Integer, primary_key=True)
    series_name = Column(String(250), nullable=False)
    description = Column(String(500), nullable=False)

    @property
    def serialize(self):
        return {
            'series_name': self.series_name,
            'description': self.description,
            'id': self.id,
        }

class Issue(Base):
    __tablename__ = 'issue'
    id = Column(Integer, primary_key=True)
    issue_name = Column(String(250), nullable = False)
    issue_number = Column(Integer, nullable = False)
    publication_date = Column(Date,nullable = False)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable = False)
    series_id = Column(Integer, ForeignKey('series.id'), nullable = False)

    @property
    def serialize(self):
        return {
            'issue_name' : self.issue_name,
            'issue_number' : self.issue_number,
            'publication_date' : self.publication_date,
            'artist_id': self.artist_id,
            'series_id': self.series_id,
            'id': self.id
        }

# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///xpress_publishing.db')
Base.metadata.create_all(engine)