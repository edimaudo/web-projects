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

class Menu(Base):
    __tablename__ = 'menu'
    id = Column(Integer, primary_key=True)
    title = Column(Integer, nullable = False)
    menu_items = relationship('MenuItem', backref='menu')

    @property
    def serialize(self):
        return {
            'title': self.title,
            'id': self.id,
        }

class MenuItem(Base):
    __tablename__ = 'menuitem'
    id = Column(Integer, primary_key=True)
    menu_item_name = Column(String(250), nullable = False)
    description = Column(String(250))
    inventory = Column(Integer, nullable = False)
    price = Column(Float, nullable = False)
    menu_id = Column(Integer, ForeignKey('menu.id'), nullable = False)

    @property
    def serialize(self):
        return {
            'menu_item_name' : self.menu_item_name,
            'description' : self.description,
            'inventory' : self.inventory,
            'price' : self.price,
            'id': self.id
        }

# creates a create_engine instance at the bottom of the file
engine = create_engine('sqlite:///expresso.db')
Base.metadata.create_all(engine)