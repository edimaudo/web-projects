"""Adds all minerals from .json data file to database."""
import json
from minerals import db
from minerals.models import Minerals

filename = 'minerals.json'
with open(filename, encoding='utf-8') as file:
    minerals = json.load(file)

for mineral in minerals:
    Minerals.create(
        name = mineral['name'],
        img_filename = mineral['image filename'],
        img_caption = mineral['image caption'],
        category = mineral['category'],
        formula = mineral['formula'],
        strunz_classification = mineral['strunz classification'],
        crystal_system = mineral['crystal system'],
        unit_cell = mineral['unit cell'],
        color = mineral['color'],
        crystal_symmetry = mineral['crystal symmetry'],
        cleavage = mineral['cleavage'],
        mohs_hardness = mineral['mohs scale hardness'],
        luster = mineral['luster'],
        streak = mineral['streak'],
        diaphaneity = mineral['diaphaneity'],
        optical_properties = mineral['optical properties'],
        refractive_index = mineral['refractive index'],
        crystal_habit = mineral['crystal habit'],
        specific_gravity = mineral['specific gravity']
    )