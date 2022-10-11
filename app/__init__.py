import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import configparser

config = configparser.ConfigParser(default_section=None)
config.read('conf/config.conf', encoding='utf-8')

# APP AND CONFIG
#########################
app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

#app.config['SECRET_KEY'] = config["flask"]["secret_key"]
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, config["flask"]["db_name"])
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = config["flask"]["track_modifications"]

app.config['SECRET_KEY'] = 'mysecretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQL DATABASE AND MODELS
#########################
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# ROUTING
#########################
from app import routes
