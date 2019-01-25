'''This file contains the different meetup endpoints. create_meetup(),  get_all_meetups(),  get_one_meetup(), 
delete_meetup()'''

from flask import request, jsonify, abort
from flask_restful import Resource, reqparse
from ..utils.validator import validate, datetime
from ..models.meetup_models import Meetups
from datetime import datetime
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity
)
import re

meetups_db = Meetups()


class Meetup(Resource):
    '''This class handles the meetup endpoints'''

    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        user_data = request.get_json()
        data = validate(user_data, required_fields=[
                        'location', 'images', 'topic', 'happening_on'])
        if type(data) == list:
            return {"status": 400, "errors": data},
        location = data["location"]
        images = data["images"]
        topic = data['topic']
        happening_on = data['happening_on']
        if not re.match(r"^[A-Za-z][a-zA-Z]", location):
            return {"status": 400, "message": "Location cannot be characters!"}, 400
        if not re.match(r"^[A-Za-z][a-zA-Z]", topic):
            return {"status": 400, "message": "Topic cannot be characters!"}, 400
        created_meetup = meetups_db.create_meetup(
            location, images, topic, happening_on, current_user)
        if (created_meetup):
            return {"status": 201, "data": created_meetup}, 201

    def get(self):
        all_meetups = meetups_db.get_all_meetups()
        return {"status": 200, "data": all_meetups}, 200


class SingleMeetup(Meetup):
    def get(self, id):
        single_meetup = meetups_db.get_one_meetup(id)
        if (single_meetup):
            return {"status": 200, "data": single_meetup}
        return {"status": 404, "message": "Meetup with id {} doesn't exist!".format(id)}, 404

    def delete(self, id):
        deleted_meetup = meetups_db.delete_meetup(id)
        if (deleted_meetup):
            return {"status": 200, "message": "Meetup {} has been deleted!".format(id)}
        return {"status": 404, "message": "Meetup with id {} doesn't exist!".format(id)}, 404
