from app import app
from flask import render_template, flash, redirect, url_for, request
from app import db
from app.models import Pokemon



@app.route('/')
@app.route('/index')
def index():
    return "hello world"


#index route

#search route


#filter route