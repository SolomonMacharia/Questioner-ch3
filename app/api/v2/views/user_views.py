from flask import request, jsonify, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, reqparse
from ..utils.validator import validate
from ..models.user_models import Users
import re

user_db = Users() 


class User(Resource):
    def post(self):
        # import pdb; pdb.set_trace()
        user_data = request.get_json()
        data = validate(user_data, required_fields=['username', 'email', 'password', 'confirm_password'])
        if type(data) == list:
            return {"status": 400, "errors": data}, 
            
        username = data["username"]
        email = data["email"]
        password = data["password"]
        confirm_password = data["confirm_password"]

        if password != confirm_password:
            abort(400, "Passwords do not much!")

        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            abort(400, "Incorrect email format!")
        
        user_db.create_user(username, email.lower(), generate_password_hash(password), check_password_hash(password, confirm_password))
        return {"status": 201, "Message": "User {} created!". format(username)}, 201

    def get(self):
        pass


class SingleUser(User):
    pass
