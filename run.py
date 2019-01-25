from app import create_app
import os
from flask_jwt_extended import JWTManager

environment = os.getenv('APP_ENV')

app = create_app(environment)

jwt = JWTManager(app)
