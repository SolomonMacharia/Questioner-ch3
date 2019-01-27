from flask import Flask, make_response
from flask_restful import Api
from .views.user_views import User, SingleUser, UserLogin
from .views.meetup_views import Meetup, SingleMeetup
from .views.question_views import Questions, SingleQuestion, DownvoteQuestion
from flask import Blueprint

version_two_bp = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version_two_bp)
api.add_resource(User, '/users')
api.add_resource(Meetup, '/meetups')
api.add_resource(SingleMeetup, '/meetups/<int:id>')
api.add_resource(Questions, '/questions')
api.add_resource(SingleQuestion, '/questions/upvote/<int:id>')
api.add_resource(DownvoteQuestion, '/questions/downvote/<int:id>')
api.add_resource(SingleUser, '/users/<int:id>')
api.add_resource(UserLogin, '/auth/login')


@version_two_bp.errorhandler(405)
def bad_request(error):
    """Error to catch not allowed method"""
    return {"status": 405, "error": "Method not allowed!"}, 405


@version_two_bp.errorhandler(500)
def internal_server_error(error):
    """Error to catch internal server error"""
    return {"status": 500, "error": "Internal error!"}, 500


@version_two_bp.errorhandler(404)
def not_found(error):
    """Error to catch page not found"""
    return {"status": 404, "error": "Resource not found!"}, 404
