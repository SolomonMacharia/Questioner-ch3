'''This file contains the different meetup endpoints. create_meetup(),  get_all_meetups(),  get_one_meetup(), 
delete_meetup()'''

from flask import request, jsonify, abort
from flask_restful import Resource, reqparse
from ..utils.validator import validate
from ..models.meetup_models import Meetups
from datetime import datetime
import re

meetups_db = Meetups() 

class Meetup(Resource):
    '''This class handles the meetup endpoints'''
    def post(self):
        # import pdb; pdb.set_trace()
        user_data = request.get_json()
        data = validate(user_data, required_fields=['location', 'images', 'topic', 'happening_on'])
        if type(data) == list:
            return {"status": 400, "errors": data}, 
        location = data["location"]
        images = data["images"]
        topic = data['topic']
        happening_on = data['happening_on']

        meetups_db.create_meetup( location, images, topic, happening_on)
        return {"status": 201, "Message": "Meetup ' {} ' created!". format(topic)}, 201

    def get(self):
        all_meetups = meetups_db.get_all_meetups()
        return {"status": 200, "data": all_meetups}, 200

class SingleMeetup(Meetup):
    def get(self, id):
        single_meetup = meetups_db.get_one_meetup(id)
        return {"status": 200, "data": single_meetup}

        
