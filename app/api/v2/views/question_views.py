from flask import request, jsonify, abort
from flask_restful import Resource, reqparse
from ..utils.validator import validate
from ..models.meetup_models import Meetups
from ..models.question_models import QuestionModels
from datetime import datetime
import re

questions_db = QuestionModels()

class Questions(Resource):
    '''This class handles the questions endpoints'''
    def post(self):
        # import pdb; pdb.set_trace()
        user_data = request.get_json()
        data = validate(user_data, required_fields=['title', 'body', 'votes'])
        if type(data) == list:
            return {"status": 400, "errors": data}, 400
        title = data["title"]
        body = data['body']
        votes = data['votes']

        questions_db.create_question( title, body, votes)
        return {"status": 201, "Message": "Question ' {} ' created!". format(title)}, 201
    def get(self):
        all_questions = questions_db.fetch_all_questions()
        return {"status": 200, "data": all_questions}, 200
