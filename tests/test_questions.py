import os
import unittest
from flask_jwt_extended import JWTManager

import json
from app import create_app
from migrate import create_tables, drop_tables


class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        JWTManager(self.app)
        self.client = self.app.test_client()

        self.question = json.dumps({
            'meetupId': 342,
            'title': 'Learn python today',
            'body': 'Snakes terrify me!'
        })

        self.headers = {
            'Content-Type': 'application/json',
        }

        # create a user for tests
        self.client.post(
            '/api/v2/users', data=self.question, headers=self.headers)

        # login test user
        login_data = self.client.post(
            '/api/v2/auth/login', data=self.question, headers=self.headers).get_data()

        self.access_token = json.load(login_data)['access_token']
        login_message = json.loads(login_data.get_data())
        self.assertEqual(login_message['message'], "login success")


    # def test_question_creation(self):
    #     resp = self.client.post(
    #         '/api/v2/meetups', data=json.dumps(self.question), content_type='application/json')
    #     self.assertEqual(resp.status_code, 201)

    # def test_get_all_questions(self):
    #     resp = self.client.get(
    #         '/api/v2/questions', data=json.dumps(self.question), content_type='application/json')
    #     self.assertEqual(resp.status_code, 200)

    # def test_upvote_question(self):
        # resp = self.client.get('/api/v2/questions', data=json.)

    def tearDown(self):
        print('Dropping Tables')
        drop_tables()
        # pass


if __name__ == '__main__':
    unittest.main()
