import os
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
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
login.login_message = 'Please log in to access this page'

# for send mail
if not app_inst.debug:
    if app_inst.config['MAIL_SERVER']:
        auth = None
        if app_inst.config['MAIL_USERNAME'] or app_inst.config['MAIL_PASSWORD']:
            auth = (app_inst.config['MAIL_USERNAME'], app_inst.config['MAIL_PASSWORD'])
        secure = None
        if app_inst.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app_inst.config['MAIL_SERVER'], app_inst.config['MAIL_PORT']),
            fromaddr='no-reply@' + app_inst.config['MAIL_SERVER'],
            toaddrs=app_inst.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        app_inst.logger.addHandler(mail_handler)

        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
                                           backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app_inst.logger.addHandler(file_handler)

        app_inst.logger.setLevel(logging.INFO)
        app_inst.logger.info('Microblog startup')

from app import routes, models, errors
