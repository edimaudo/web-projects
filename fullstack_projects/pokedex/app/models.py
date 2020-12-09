from app import db

class Pokemon(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(120))
    Type1 = db.Column(db.String(120))
    Type2 = db.Column(db.String(120))
    Total = db.Column(db.Integer)
    HP = db.Column(db.Integer)
    Attack = db.Column(db.Integer)
    Defense = db.Column(db.Integer)
    Special_Attack = db.Column(db.Integer)
    Special_Defense = db.Column(db.Integer)
    Speed = db.Column(db.Integer)
    Generation = db.Column(db.Integer)
    Legendary = db.Column(db.String(120))

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
    
    def load_csv():
        import csv 
        filename = "pokemon.csv"
        pokemon_info = []
        with open(filename, encoding='utf-8') as file:
            data = csv.reader(csv_file, delimiter=',')
            first_line = True
        
        for row in data:
            if not first_line:
                entry_data = Pokemon(Name = Pokemon['Name'],
                Type1 = Pokemon['Type1'],
                Type2 = Pokemon['Type2'],
                Total = Pokemon['Total'],
                HP = Pokemon['HP'], 
                Attack = Pokemon['Attack'],
                Defense = Pokemon['Defense'],
                Special_Attack = Pokemon['Special_Attack'],
                Special_Defense = Pokemon['Special_Defense'],
                Speed = Pokemon['Speed'],
                Generation = Pokemon['Generation'],
                Legendary = Pokemon['Legendary']
                )
                pokemon_info.append(entry_data)
            else:
                first_line == FALSE
        db.session.add_all(pokemon_info)
        db.session.commit()
