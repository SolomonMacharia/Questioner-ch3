import unittest
import json
from app import create_app
from migrate import create_tables, drop_tables

class TestUsers(unittest.TestCase):
    def setUp(self):
        self.app = create_app(app_settings='testing')
        self.client = self.app.test_client()
        self.app.testing = True
        self.db_url = ''
    
        self.user = {
            'username': 'solomon',
            'email': 'solomon@example.email',
            'password': 'python',
            'confirm_password': 'python'
        }

    def tearDown(self):
        # drop_tables()
        pass
        
    def test_user_registration(self):
        resp = self.client.post('/api/v2/users', data=json.dumps(self.user), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        


if __name__ == '__main__':
    unittest.main()