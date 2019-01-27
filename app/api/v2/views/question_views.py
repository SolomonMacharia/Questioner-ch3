from flask import request, jsonify, abort
from flask_restful import Resource, reqparse
from ..utils.validator import validate
from ..models.meetup_models import Meetups
from ..models.question_models import QuestionModels
from ..models.meetup_models import Meetups
from datetime import datetime
from flask_jwt_extended import (
    jwt_required, create_access_token,
    get_jwt_identity
)
import re

questions_db = QuestionModels()
meetup_db = Meetups()


class Questions(Resource):
    '''This class handles the questions endpoints'''
    @jwt_required
    def post(self):
        current_user = get_jwt_identity()
        user_data = request.get_json()
        data = validate(user_data, required_fields=[
                        'title', 'body', 'meetup_id'])
        if type(data) == list:
            return {"status": 400, "errors": data}, 400
        title = data["title"]
        body = data['body']
        meetup_id = data['meetup_id']

        if not re.match(r"^[A-Za-z][a-zA-Z]", title):
            return {"status": 400, "message": "Title should contain alphanumeric characters!"}, 400
        if not re.match(r"^[A-Za-z][a-zA-Z]", body):
            return {"status": 400, "message": "Body should contain alphanumeric characters"}, 400
        if not re.match(r"^[0-9]", meetup_id):
            return {"status": 400, "message": "Body should contain alphanumeric characters"}, 400

        meetup = meetup_db.get_one_meetup(meetup_id)

        if not meetup:
            return {"status": 400, "message": "No meetup with id {}".format(meetup_id)}, 400

        created_question = questions_db.create_question(
            title, body, meetup_id, current_user)

        if (created_question):
            return {"status": 201, "data": created_question}, 201

    def get(self):
        all_questions = questions_db.fetch_all_questions()
        return {"status": 200, "data": all_questions}, 200


class SingleQuestion(Questions):
    def patch(self, id):
        upvoted = questions_db.upvote_question(id)
        if (upvoted):
            return {"status": 200, "data": upvoted}, 200


class DownvoteQuestion(Resource):
    def patch(self, id):
        downvoted = questions_db.downvote_question(id)
        if downvoted:
            return {"status": 200, "data": downvoted}, 200
