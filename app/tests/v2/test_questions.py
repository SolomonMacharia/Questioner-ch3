import os
import unittest
import json
from app import create_app
from migrate import create_tables, drop_tables

class TestQuestions(unittest.TestCase):
    def setUp(self):
        # import pdb; pdb.set_trace()
        self.app = create_app(environment='testing')
        self.client = self.app.test_client()
        self.app.testing = True
    
        self.question = {
            'title': 'title',
            'body': 'body'
        }

    def test_question_creation(self):
        resp = self.client.post('/api/v2/meetups', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(resp.status_code, 201)

    def test_get_all_questions(self):
        resp = self.client.get('/api/v2/questions', data=json.dumps(self.question), content_type='application/json')
        self.assertEqual(resp.status_code, 200)

 
    def tearDown(self):
        print('Dropping Tables')
        drop_tables()
        # pass

if __name__ == '__main__':
    unittest.main()
