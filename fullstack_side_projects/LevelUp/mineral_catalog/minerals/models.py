from minerals import db

class Minerals(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))
	img_filename = db.Column(db.String(255))
	img_caption = db.Column(db.String(255))
	category = db.Column(db.String(255))
	formula = db.Column(db.String(255))
	strunz_classification = db.Column(db.String(255))
	crystal_system = db.Column(db.String(255))
	unit_cell = db.Column(db.String(255))
	color = db.Column(db.String(255))
	crystal_symmetry = db.Column(db.String(255))
	cleavage = db.Column(db.String(255))
	mohs_hardness = db.Column(db.String(255))
	luster = db.Column(db.String(255))
	streak = db.Column(db.String(255))
	diaphaneity = db.Column(db.String(255))
	optical_properties = db.Column(db.String(255))
	refractive_index = db.Column(db.String(255),default='')
	crystal_habit = db.Column(db.String(255),default='')
	specific_gravity = db.Column(db.String(255),default='')
	
	def __repr__(self):
		return '<Minerals {}>'.format(self.name) 
    
    # def add_minerals(self):
    #     import json
    #     filename = 'minerals.json'

    #     with open(filename, encoding='utf-8') as file:
    #         minerals = json.load(file)

    #     for mineral in minerals:
    #         Mineral.create(
    #             name = mineral['name'],
    #             img_filename = mineral['image filename'],
    #             img_caption = mineral['image caption'],
    #             category = mineral['category'],
    #             formula = mineral['formula'],
    #             strunz_classification = mineral['strunz classification'],
    #             crystal_system = mineral['crystal system'],
    #             unit_cell = mineral['unit cell'],
    #             color = mineral['color'],
    #             crystal_symmetry = mineral['crystal symmetry'],
    #             cleavage = mineral['cleavage'],
    #             mohs_hardness = mineral['mohs scale hardness'],
    #             luster = mineral['luster'],
    #             streak = mineral['streak'],
    #             diaphaneity = mineral['diaphaneity'],
    #             optical_properties = mineral['optical properties'],
    #             refractive_index = mineral['refractive index'],
    #             crystal_habit = mineral['crystal habit'],
    #             specific_gravity = mineral['specific gravity']
    #         )

    #     return ""


                ##     """Adds all minerals from .json data file to database."""