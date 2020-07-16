# app/__init__.py

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
from flask import request, jsonify, abort

# local import
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()




def create_app(config_name):
	from api.models import Artist, Issue, Series
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    @app.route('/Artists/', methods=['POST', 'GET'])
    def Artists():
        if request.method == "POST":
            artist_name = str(request.data.get('artist_name', ''))
            if artist_name:
                artist = Artist(artist_name=artist_name)
                artist.save()
                response = jsonify({
                    'id': artist.id,
                    'artist_name': artist.artist_name,
                    'date_of_birth': artist.date_of_birth,
                    'biography': artist.biography,
                    'is_currently_employed': artist.is_currently_employed
                })
                response.status_code = 201
                return response
        else:
            # GET
            artists = Artist.get_all()
            results = []

            for artist in artists:
                obj = {
                    'id': artist.id,
                    'artist_name': artist.artist_name,
                    'date_of_birth': artist.date_of_birth,
                    'biography': artist.biography,
                    'is_currently_employed': artist.is_currently_employed
                }
                results.append(obj)
            response = jsonify(results)
            response.status_code = 200
            return response

    ###################################
    # The GET and POST code is here
    ###################################

    @app.route('/Artist/<int:id>', methods=['GET', 'PUT', 'DELETE'])
    def Artist_manipulation(id, **kwargs):
     # retrieve a buckelist using it's ID
        artist = Artist.query.filter_by(id=id).first()
        if not artist:
            # Raise an HTTPException with a 404 not found status code
            abort(404)

        if request.method == 'DELETE':
            Artist.delete()
            return {
            "message": "Artist {} deleted successfully".format(artist.id) 
         }, 200

        elif request.method == 'PUT':
            name = str(request.data.get('artist_name', ''))
            artist.name = name
            artist.save()
            response = jsonify({
                    'id': artist.id,
                    'artist_name': artist.artist_name,
                    'date_of_birth': artist.date_of_birth,
                    'biography': artist.biography,
                    'is_currently_employed': artist.is_currently_employed
            })
            response.status_code = 200
            return response
        else:
            # GET
            response = jsonify({
                    'id': artist.id,
                    'artist_name': artist.artist_name,
                    'date_of_birth': artist.date_of_birth,
                    'biography': artist.biography,
                    'is_currently_employed': artist.is_currently_employed
            })
            response.status_code = 200
            return response

    return app