import os
from flask import Flask
from .api.v2 import version_two_bp, internal_server_error, bad_request, not_found
from app.config import APP_SETTINGS
from migrate import create_tables
from flask_jwt_extended import JWTManager


def create_app(environment=''):
    app = Flask(__name__)
    create_tables()
    app.config.from_object(APP_SETTINGS[environment])
    app.register_blueprint(version_two_bp)
    app.register_error_handler(404, not_found)
    app.register_error_handler(405, bad_request)
    app.register_error_handler(500, internal_server_error)
    return app
