import unittest
import json
from app import create_app
from flask_jwt_extended import JWTManager
from migrate import create_tables, drop_tables


class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        JWTManager(self.app)
        self.client = self.app.test_client()

        self.user = json.dumps({
            'username': 'solomon',
            'email': 'solomon@example.email',
            'password': 'python',
            'confirm_password': 'python'
        })

        self.headers = {
            'Content-Type': 'application/json',
        }

    def test_user_registration(self):
        resp = self.client.post(
            '/api/v2/users', data=self.user, headers=self.headers)
        self.assertEqual(resp.status_code, 201)

    def test_invalid_email(self):
        payload = {'email': 'sol',
                   'password': 'python'}
        resp = self.client.post(
            '/api/v2/auth/login', data=json.dumps(payload), headers=self.headers)
        self.assertEqual(resp.status_code, 400)
        res = json.loads(resp.get_data())
        self.assertEqual(res['message'], 'Incorrect email format!')

    def tearDown(self):
        drop_tables()


if __name__ == '__main__':
    unittest.main()
