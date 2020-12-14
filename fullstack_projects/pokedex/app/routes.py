from app import app
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app import db
from app.models import Pokemon
#from flask_httpauth import HTTPBasicAuth

#error handlers
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request'}),400)

@app.errorhandler(404):
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}),404)

#index route
@app.route('/')
@app.route('/index')
def index():
    return "hello world"
#search route


#filter route