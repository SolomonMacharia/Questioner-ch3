import os
from flask import Flask
from .api.v2 import version_two_bp
from app.config import APP_SETTINGS


def create_app(environment=''):
    app = Flask(__name__)
    app.config.from_object(APP_SETTINGS[environment])
    app.register_blueprint(version_two_bp)
    return app
