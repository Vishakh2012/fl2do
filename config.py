from os import environ 

class Config:
    """base configutation"""
    debug =True
    SECRET_KEY = environ['SECRET_KEY']
    SESSION_COOKIE_NAME = environ.get('SESSION_COOKIE_NAME')
    SESSION_COOKIE_PATH = '/'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SQLALCHEMY_DATABASE_URI = environ.get('DATABSE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False
    DATABSE_URI = environ.get('PROD_DATABASE_URI')

class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
    
    
    
