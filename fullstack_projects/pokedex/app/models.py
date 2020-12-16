from app import db

class Pokemon(db.Model):

    __tablename__ = 'pokemon'
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255))
    Type1 = db.Column(db.String(255))
    Type2 = db.Column(db.String(255))
    Total = db.Column(db.Integer)
    HP = db.Column(db.Integer)
    Attack = db.Column(db.Integer)
    Defense = db.Column(db.Integer)
    Special_Attack = db.Column(db.Integer)
    Special_Defense = db.Column(db.Integer)
    Speed = db.Column(db.Integer)
    Generation = db.Column(db.Integer)
    Legendary = db.Column(db.String(255))

    @property
    def serialize(self):
        return {
            'Name': self.Name,
            'Type1':self.Type1,
            'Type2':self.Type2,
            'Total':self.Total,
            'HP':self.HP,
            'Attack':self.Attack,
            'Defense': self.Defense,
            'Special_Attack': self.Special_Attack,
            'Special_Defense': self.Special_Defense,
            'Speed':self.Speed,
            'Generation':self.Generation,
            'Legendary': self.Legendary
        }

    # def __init__(self, Name, Type1, Type2, Total, HP, Attack, Defense, Special_Attack, Special_Defense, Speed, Generation, Legendary):
    #     self.Name = Name
    #     self.Type1 = Type1
    #     self.Type2 = Type2
    #     self.Total = Total
    #     self.HP = HP
    #     self.Attack = Attack
    #     self.Defense = Defense
    #     self.Special_Attack = Special_Attack
    #     self.Special_Defense = Special_Defense
    #     self.Speed = Speed
    #     self.Generation = Generation
    #     self.Legendary = Legendary
    
    def __repr__(self):
        return '<Pokemon {}>'.format(self.Name)

 #load data   
    def load_pokemon():
        import csv 
        import pandas as pd
        pokemons = pd.read_csv("pokemon.csv")
        pokemon_info = []
        for i,pokemon in pokemons.iterrows():
            entry_data = Pokemon(Name = pokemon['Name'],Type1 = pokemon['Type1'],Type2 = pokemon['Type2'],Total = pokemon['Total'],HP = pokemon['HP'], Attack = pokemon['Attack'],Defense = pokemon['Defense'],Special_Attack = pokemon['Special_Attack'],Special_Defense = pokemon['Special_Defense'],Speed = pokemon['Speed'],Generation = pokemon['Generation'],Legendary = pokemon['Legendary'])
            pokemon_info.append(entry_data)
        db.session.add_all(pokemon_info)
        db.session.commit()

        





