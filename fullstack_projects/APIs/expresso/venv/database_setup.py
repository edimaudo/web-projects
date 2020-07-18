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



Menu
id - Integer, primary key, required
title - Text, required

MenuItem
id - Integer, primary key, required
name - Text, required
description - Text, optional
inventory - Integer, required
price - Integer, required
menu_id - Integer, foreign key, required

class Employee(Base):
    __tablename__ = 'employee'
    id = Column(Integer, primary_key=True)
    employee_name = Column(String(250), nullable= False)
    position = Column(String(250), nullable= False)
    wage = Column(Float, nullable = False)
    is_currently_employee = Column(Integer, default = 1)
    timesheets = relationship('Timesheet', backref='employee')

    @property
    def serialize(self):
        return {
            'employee_name': self.artist_name,
            'position': self.position,
            'wage': self.wage,
            'is_currently_employee': self.is_currently_employee,
            'id':self.id,
        }

class Timesheet(Base):
    __tablename__ = 'timesheet'
    id = Column(Integer, primary_key=True)
    hours = Column(Integer, nullable = False)
    rate = Column(Integer, nullable = False)
    date = Column(DateTime, nullable = False)
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable = False)

    @property
    def serialize(self):
        return {
            'hours': self.hours,
            'rate': self.rate,
            'date': self.date,
            'id': self.id,
        }

class Issue(Base):
    __tablename__ = 'issue'
    id = Column(Integer, primary_key=True)
    issue_name = Column(String(250), nullable = False)
    issue_number = Column(Integer, nullable = False)
    publication_date = Column(String(10), nullable = False)
    artist_id = Column(Integer, ForeignKey('artist.id'), nullable = False)
    series_id = Column(Integer, ForeignKey('series.id'), nullable = False)

    @property
    def serialize(self):
        return {
            'issue_name' : self.issue_name,
            'issue_number' : self.issue_number,
            'publication_date' : self.publication_date,
            'id': self.id
        }

# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///expresso.db')
Base.metadata.create_all(engine)