import os
from flask import Flask
from .api.v2 import version_two_bp
from app.config import APP_SETTINGS
from migrate import create_tables
from flask_jwt_extended import JWTManager

def create_app(environment=''):
    app = Flask(__name__)
    create_tables()
    app.config.from_object(APP_SETTINGS[environment])
    jwt = JWTManager(app)
    app.register_blueprint(version_two_bp)
    return app
