from django.db import models


class Mineral(models.Model):
    name = models.CharField(max_length=255)
    img_filename = models.CharField(max_length=255)
    img_caption = models.TextField(max_length=255)
    category = models.CharField(max_length=255)
    formula = models.CharField(max_length=255)
    strunz_classification = models.CharField(max_length=255)
    crystal_system = models.CharField(max_length=255)
    unit_cell = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    crystal_symmetry = models.CharField(max_length=255)
    cleavage = models.CharField(max_length=255)
    mohs_hardness = models.CharField(max_length=255)
    luster = models.CharField(max_length=255)
    streak = models.CharField(max_length=255)
    diaphaneity = models.CharField(max_length=255)
    optical_properties = models.CharField(max_length=255)
    refractive_index = models.CharField(max_length=255, blank=True, default='')
    crystal_habit = models.CharField(max_length=255, blank=True, default='')
    specific_gravity = models.CharField(max_length=255, blank=True, default='')


    def __str__(self):
        return self.name


    def add_minerals(self):
        """Adds all minerals from .json data file to database."""
        import json
        filename = 'minerals.json'

        with open(filename, encoding='utf-8') as file:
            minerals = json.load(file)

        for mineral in minerals:
            Mineral.create(
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
