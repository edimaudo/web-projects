from app import db

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True)
    Country = db.Column(db.String(255),unique=True, nullable=False)
    Code = db.Column(db.String(255),unique=True, nullable=False)
    Population = db.Column(db.Integer)
    GDP = db.Column(db.Integer)

    def __init__(self,Country,Code, Population,GDP):
        self.Country = Country
        self.Code = Code
        self.Population = Population
        self.GDP = GDP

    def __repr__(self):
        return 'Country {}>'.format(self.Country)

    def load_country_data():
        import csv
        import pandas as pd 
        countries = pd.read_csv("country.csv")
        country_info = []
        for i, country in countries.iterrows():
            entry_data = Country(Country = country['Country'], Code = country['Code'], Population = country['Population'], GDP = country['GDP'])
            country_info.append(entry_data)
        db.session.add_all(country_info)
        db.session.commit()

class Medal(db.Model):
    __tablename__ = "medal"
    id = db.Column(db.Integer, primary_key=True)
    Year = db.Column(db.Integer, nullable = False)
    City = db.Column(db.String(255), nullable=False)
    Sport = db.Column(db.String(255), nullable=False)
    Discipline = db.Column(db.String(255), nullable=False)
    Athlete = db.Column(db.String(255), nullable=False)
    Country = db.Column(db.String(255), nullable=False)
    Gender = db.Column(db.String(255), nullable=False)
    Event = db.Column(db.String(255), nullable=False)
    Medal = db.Column(db.String(255), nullable=False)
    
#Year,City,Sport,Discipline,Athlete,Country,Gender,Event,Medal

    def __init__(self, Year,City,Sport,Discipline,Athlete,Country,Gender,Event,Medal):
        self.Year = Year
        self.City = City
        self.Sport = Sport
        self.Discipline = Discipline
        self.Athlete = Athlete
        self.Country = Country
        self.Gender = Gender
        self.Event = Event
        self.Medal = Medal
    
    def __repr__(self):
        return 'Medal {}>'.format(self.City)
    
    def load_medal_data():
        import csv
        import pandas as pd 
        medals = pd.read_csv("goldmedal.csv")
        medal_info = []
        for i, medal in medals.iterrows():
            entry_data = Medal(Year = medal['Year'], City = medal['City'], Sport = medal['Sport'],Discipline = medal['Discipline'],Athlete = medal['Athlete'],Country = medal['Country'],Gender = medal['Gender'],Event = medal['Gender'],Medal = medal['Medal'])
            medal_info.append(entry_data)
        db.session.add_all(medal_info)
        db.session.commit()