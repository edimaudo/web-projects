from minerals import minerals
from flask import render_template

@minerals.route('/')
@minerals.route('/index')
def index():
    return render_template('index.html')