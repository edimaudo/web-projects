from app import db

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    Country = db.Column(db.String(255),unique=True, nullable=False)
    Code = db.Column(db.String(255),unique=True, nullable=False)
    GDP = db.Column(db.Integer)
    Population = db.Column(db.Integer)

    def __init__(self,Country,Code, GDP, Population):
        self.Country = Country
        self.Code = Code
        self.GDP = GDP
        self.Population = Population

    def __repr__(self):
        return 'Country {}>'.format(self.Country)

    def load_country_data():
        import csv
        import pandas as pd 
        countries = pd.read_csv("country.csv")
        country_info = []
        for i, country in countries.iterrows():
            entry_data = Country(Country = country['Country'],Code = country['code'],Population = country['Population'],GDP = country['GDP'])
            country_info.append(entry_data)
        db.session.add_all(country_info)
        db.session.commit()

class Medal(db.Model):
    __tablename__ = "medal"
    id = db.Column(db.Integer, primary_key=True)
    Year = db.Column(db.Integer, nullable = False)
    City = db.Column(db.String(255), nullable=False)
    Season = db.Column(db.String(255), nullable=False)
    Name = db.Column(db.String(255), nullable=False)
    Country = db.Column(db.String(255), nullable=False)
    Gender = db.Column(db.String(255), nullable=False)
    Sport = db.Column(db.String(255), nullable=False)
    Discipline = db.Column(db.String(255), nullable=False)
    Event = db.Column(db.String(255), nullable=False)

    def __init__(self, Year, City, Season, Name, Country, Gender, Sport, Discipline, Event):
        self.Year = Year
        self.City = City
        self.Season = Season
        self.Name = Name
        self.Country = Country
        self.Gender = Gender
        self.Sport = Sport
        self.Discipline = Discipline
        self.Event = Event
    
    def __repr__(self):
        return 'City {}>'.format(self.City)
    
    def load_medal_data():
        import csv
        import pandas as pd 
        medals = pd.read_csv("goldmedal.csv")
        medal_info = []
        for i, medal in medals.iterrows():
            entry_data = Medal()
            medal_info.append(entry_data)
        db.session.add_all(medal_info)
        db.session.commit()        




