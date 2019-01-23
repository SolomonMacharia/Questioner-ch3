from flask import request, jsonify, abort
from flask_restful import Resource, reqparse
from ..utils.validator import validate
from ..models.meetup_models import Meetups
from ..models.question_models import QuestionModels
from datetime import datetime
import re

questions_db = QuestionModels()

class Questions(Resource):
    '''This class handles the meetup endpoints'''
    def get(self):
        all_questions = questions_db.fetch_all_questions()
        return {"status": 200, "data": all_questions}, 200
