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

#search  - Search: name
#@app.route('/pokemon/api/search/',methods=['GET'])

#filter  #HP,Attack,Defense e.g. Filter: HP, Attack & Defense `/pokemon?hp[gte]=100&defense[lte]=200` 

#index route
@app.route('/')
@app.route('/pokemon/api/all_pokemon',methods=['GET'])
def index():
    pokemons = Pokemon.query.all()
    return jsonify({'pokemons': [make_pokemon(pokemon) for pokemon in pokemons]})

# def make_pokemon(pokemon):
#     new_pokemon = {}
#     for field in pokemon:
#         if field == 'id':
#             new_pokemon['uri'] = url_for('get_pokemon', pokemon_id=pokemon['id'],_external=True)
#         else:
#             new_pokemon[field] = pokemon[field]
#     return new_pokemon

# @app.route('/pokemon/api/v1.0/all_pokemon<int:pokemon_id>', methods=['GET'])
# def get_pokemon(pokemon_id):
#     pokemon = [pokemon for pokemon in pokemons if pokemon['id'] == pokemon_id]
#     if len(pokemon) == 0:
#         abort(404)
#     return jsonify({'pokemon': make_pokemon(pokemon[0])})

 