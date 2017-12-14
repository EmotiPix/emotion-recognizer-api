import unittest
import json
from web.server import app

class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        self.emotions_list = ["neutral", "anger", "disgust", "happy", "sadness", "surprise", "no_emotion"]

    def tearDown(self):
        pass

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_get_emotions_list(self):
        result = self.app.get('/list/emotions')
        self.assertEqual(result.data, json.dumps(self.emotions_list))


if __name__ == '__main__':
    unittest.main()