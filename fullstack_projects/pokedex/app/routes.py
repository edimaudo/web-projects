from app import app
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app import db
from app.models import Pokemon


#error handler
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}),400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}),404)

#index route
@app.route('/')
@app.route('/pokemon/api/v1/all_pokemon',methods=['GET'])
def index():
    pokemons = Pokemon.query.all()
    if len(pokemons) == 0:
        return jsonify(pokemons= [pokemon.serialize for pokemon in pokemons])
    return bad_request(400)

#search  - Search: name
@app.route('/pokemon/api/v1/search/<string:pokemon_name>',methods=['GET'])
def search_pokemon(pokemon_name):
    pokemons = Pokemon.query.filter(Pokemon.Name.contains(pokemon_name)).order_by(Pokemon.Name).all()
    if len(pokemons) == 0:
        return not_found(404)
    return jsonify(pokemons= [pokemon.serialize for pokemon in pokemons])

#filter  #HP,Attack,Defense e.g. Filter: HP, Attack & Defense `/pokemon?hp[gte]=100&defense[lte]=200` 
@app.route()
def filter_pokemon(pokemon_hp,  pokemon_attack, pokemon_defense):
    pokemons = ""
    if len(pokemons) == 0:
        return not_found(404)
    return jsonify(pokemons= [pokemon.serialize for pokemon in pokemons])


 