from app import app
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app import db
from app.models import Pokemon


def make_pokemon(pokemon):
    new_pokemon = {}
    for field in pokemon:
        if field == 'id':
            new_pokemon['uri'] = url_for('get_pokemon', pokemon_id=pokemon['id'],_external=True)
        else:
            new_pokemon[field] = pokemon[field]
    return new_pokemon

#error handlers
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}),400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}),404)

#index route
@app.route('/pokemon/api/v1.0/all_pokemon',methods=['GET'])
def index():
    all_data = Pokemon.query.all()
    return jsonify({'pokemons': [make_pokemon(pokemon) for pokemon in pokemons]})

@app.route('/pokemon/api/v1.0/all_pokemon<int:pokemon_id>', methods=['GET'])
def get_pokemon(pokemon_id):
    pokemon = [pokemon for pokemon in pokemons if pokemon['id'] == pokemon_id]
    if len(pokemon) == 0:
        abort(404)
    return jsonify({'pokemon': make_pokemon(pokemon[0])})

#search route


#filter route