import os
import psycopg2
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    ENV = 'production'
    DEBUG = False
    TESTING = False
    CSRF_ENABLED =  True
    SECRET_KEY = b'gn%\x92\x08Zp\xffZgg~\xa4\xfcY\x8b\xb4H\xebL\xd7\xa4\x80V'
    DATABASE_URL = os.getenv('DATABASE_URL')

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    DATABASE_URL = os.getenv('DEV_DATABASE_URL')

class TestingConfig(Config):
    ENV = 'testing'
    TESTING = True
    DEBUG = True
    DATABASE_URL = os.getenv('TEST_DATABASE_URL')
    
APP_SETTINGS = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig
}