from app import app
from flask import render_template, flash, redirect, url_for, request, jsonify, make_response
from app import db
from app.models import Pokemon
#from flask_httpauth import HTTPBasicAuth

#error handlers


#index route
@app.route('/')
@app.route('/index')
def index():
    return "hello world"
#search route


#filter route