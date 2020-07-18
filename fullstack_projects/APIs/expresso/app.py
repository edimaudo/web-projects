from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker