import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # debug mode
    # DEBUG=False

    # for safety
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

    # database variables
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # email server
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')

    #MAIL_SERVER='smtp.googlemail.com'
    #MAIL_PORT=587
    #MAIL_USE_TLS=1
    #MAIL_USERNAME='eldarknz'
    #MAIL_PASSWORD='Chashki14198804'

    # and
    # Go to the Less secure app access section of your Google Account. You might need to sign in.
    # https://myaccount.google.com/lesssecureapps
    # Turn Allow less secure apps off.

    # administrator list
    ADMINS = ['eldarknz@gmail.com']
