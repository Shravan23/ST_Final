import unittest
from unittest.mock import patch
from app import create_app
from app.models import User
from tests.test_config import TestConfig

class TestUserLogin(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()  # Push context here

    def tearDown(self):
        self.ctx.pop()  # Pop context here

    @patch('app.routes.User.query')
    def test_login_valid_user(self, mock_query):
        mock_user = User()
        mock_user.id = 1
        mock_user.username = 'testuser'
        mock_user.set_password('password123')
        
        mock_query.filter_by.return_value.first.return_value = mock_user
        
        response = self.client.post('/login', data={
            'username': 'testuser',
            'password': 'password123'
        }, follow_redirects=True)
        
        self.assertIn(b'Profile', response.data)

if __name__ == '__main__':
    unittest.main()