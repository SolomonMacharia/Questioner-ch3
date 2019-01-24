from flask import request, jsonify, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource, reqparse
from ..utils.validator import validate
from ..models.user_models import Users
from datetime import datetime
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity, create_refresh_token
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
            abort(400, "Incorrect email format!"), 400
        
        user_db.create_user(username, email.lower(), generate_password_hash(password), check_password_hash(password, confirm_password))
        return {"status": 201, "Message": "User {} created!". format(username)}, 201

    def get(self):
        users = user_db.get_all_user()
        return {'status':200, 'data': users}
    

class SingleUser(User):
    def get(self, id):
        single_user = user_db.get_single_user(id)
        return {"status": 200, "data": single_user}

class UserLogin(Resource):
    def post(self):
        user_data = request.get_json()
        username = user_data["username"]
        password = user_data["password"]
        current_user = user_db.get_user_by_username(username)
        data = validate(user_data, required_fields=['username', 'password', 'confirm_password'])
        if type(data) == list:
            return {"status": 400, "errors": data}, 400
        if not current_user:
            abort(404, "User {} doesn't exist!".format(username))
        if  check_password_hash(current_user['password'], user_data['password']):
            access_token = create_access_token(identity=user_data['username'])
            return {'message': 'login success', 'access_token': access_token}, 200
        abort(401, "Invalid credentials!")
        return None
            

