from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

# app
app_inst = Flask(__name__)

# config from config.py
app_inst.config.from_object(Config)

# database
db       = SQLAlchemy(app_inst)
migrate  = Migrate(app_inst, db)

# login
login            = LoginManager(app_inst)
login.login_view = 'login'

from app import routes, models
