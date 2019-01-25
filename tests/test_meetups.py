import unittest
import json
from flask_jwt_extended import JWTManager
from app import create_app
from migrate import create_tables, drop_tables


class Testmeetups(unittest.TestCase):
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

        self.meetup = json.dumps({
            "happening_on": "The day",
            "images": "images",
            "location": "The venue",
            "topic": "Team collaboration"
        })

        self.headers = {
            'Content-Type': 'application/json',
        }

        # create a user for tests
        self.client.post(
            '/api/v2/users', data=self.user, headers=self.headers)

        # login test user
        login_data = self.client.post(
            '/api/v2/auth/login', data=self.user, headers=self.headers).get_data()

        self.access_token = json.loads(login_data)['access_token']
        self.headers.update(
            {'Authorization': 'Bearer {}'.format(self.access_token)})

    def test_meetup_creation(self):
        resp = self.client.post(
            '/api/v2/meetups', data=self.meetup, headers=self.headers)
        self.assertEqual(resp.status_code, 201)
        response_data = json.loads(resp.get_data())
        self.assertEqual(response_data['data']['topic'], 'Team collaboration')

    def test_get_all_meetups(self):
        initial_meetups = self.client.get(
            '/api/v2/meetups', headers=self.headers)
        initial_count = len(json.loads(initial_meetups.get_data())['data'])
        self.assertEqual(initial_count, 0)

        resp = self.client.post(
            '/api/v2/meetups', data=self.meetup, headers=self.headers)
        self.assertEqual(resp.status_code, 201)
        after_insert_count = json.loads(
            resp.get_data())

        self.assertNotEqual(after_insert_count, 0)

    # def test_get_specific_meetups(self):
        # response = self.client.post(
        #     '/api/v2/meetups', data=self.meetup, headers=self.headers)

        # resp = self.client.get('/api/v2/meetups/1',
        #                        headers=self.headers)
        # specific_meetup = json.loads(resp.get_data())
        # print('qqq', specific_meetup)
        # self.assertEqual(specific_meetup['data']
        #                  ['topic'], 'Team collaboration')

        #     def test_delete_meetups(self):
        #         resp = self.client.post(
        #             '/api/v2/meetups', data=json.dumps(self.meetup), content_type='application/json')
        #         self.assertEqual(resp.status_code, 201)
        #         resp = self.client.delete(
        #             '/api/v2/meetups/1', content_type='application/json')
        #         self.assertEqual(resp.status_code, 200)
        #         resp = json.loads(resp.data)
        #         self.assertEqual(resp['Message'], "Meetup 1 has been deleted!")

    def tearDown(self):
        drop_tables()


if __name__ == '__main__':
    unittest.main()
