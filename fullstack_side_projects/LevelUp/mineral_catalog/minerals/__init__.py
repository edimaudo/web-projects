from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

minerals = Flask(__name__)
minerals.config.from_object(Config)

db = SQLAlchemy(minerals)
migrate = Migrate(minerals, db)

from minerals import routes, models