from app import app
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app import db
from app.models import Pokemon

#error handlers
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}),400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}),404)

#index route
@app.route('/')
@app.route('/pokemon/api/all_pokemon',methods=['GET'])
def index():
    pokemons = Pokemon.query.all()
    return jsonify(pokemons= [pokemon.serialize for pokemon in pokemons])

#search  - Search: name
#@app.route('/pokemon/api/search/',methods=['GET'])

#filter  #HP,Attack,Defense e.g. Filter: HP, Attack & Defense `/pokemon?hp[gte]=100&defense[lte]=200` 


 