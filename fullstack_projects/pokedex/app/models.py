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

    def __init__(self, Name, Type1, Type2, Total, HP, Attack, Defense, Special_Attack, Special_Defense, Speed, Generation, Legendary):
        self.Name = Name
        self.Type1 = Type1
        self.Type2 = Type2
        self.Total = Total
        self.HP = HP
        self.Attack = Attack
        self.Defense = Defense
        self.Special_Attack = Special_Attack
        self.Special_Defense = Special_Defense
        self.Speed = Speed
        self.Generation = Generation
        self.Legendary = Legendary
    
    def __repr__(self):
        return '<Pokemon {}>'.format(self.name)
    
    def load_pokemon():
        import csv 
        filename = "pokemon.csv"
        
        with open(filename, encoding='utf-8') as file:
            pokemons = csv.reader(file, delimiter=',')
            pokemon_info = []
            for pokemon in pokemons:
                entry_data = Pokemon(Name = pokemon[0],
                    Type1 = pokemon[1],
                    Type2 = pokemon[2],
                    Total = pokemon[3],
                    HP = pokemon[4], 
                    Attack = pokemon[5],
                    Defense = pokemon[6],
                    Special_Attack = pokemon[7],
                    Special_Defense = pokemon[8],
                    Speed = pokemon[9],
                    Generation = pokemon[10],
                    Legendary = pokemon[11]
                    )
                pokemon_info.append(entry_data)
            db.session.add_all(pokemon_info)
            db.session.commit()