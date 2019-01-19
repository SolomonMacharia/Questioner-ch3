from flask import request
from flask_restful import Resource
from ..models.user_models import Users


class User(Resource, User):
    def post(self):
        data = request.get_json()
        username = data['username']
        email = data['email']
        password = data['password']
        confirm_password = data['confirm_password']

        if data:
            new_user = User.create_user(
                username, email, password, confirm_password)

            return jsonify("status": 200, "data": new_user)

    def get(selfs):
        pass


class SingleUser(User):
    pass
