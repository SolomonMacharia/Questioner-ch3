from flask import Flask
from flask_restful import Api
from .views.user_views import User, SingleUser, UserLogin
from .views.meetup_views import Meetup, SingleMeetup
from .views.question_views import Questions
from flask import Blueprint

version_two_bp = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version_two_bp)
api.add_resource(User, '/users')
api.add_resource(Meetup, '/meetups')
api.add_resource(SingleMeetup, '/meetups/<int:id>')
api.add_resource(Questions, '/questions')
api.add_resource(SingleUser, '/users/<int:id>')
api.add_resource(UserLogin, '/auth/login')
