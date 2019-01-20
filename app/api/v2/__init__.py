from flask import Flask
from flask_restful import Api
from .views.user_views import User
from flask import Blueprint

version_two_bp = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version_two_bp)
api.add_resource(User, '/users')
