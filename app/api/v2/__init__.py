from flask import Flask
from .models.user_models import Users
from flask import Blueprint

version_two_bp = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version_two_bp)
api.add_resource(Users, '/users')
