import unittest
from unittest.mock import patch
from flask import session
from app import create_app
from tests.test_config import TestConfig

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.app = create_app(TestConfig)
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()

    def tearDown(self):
        self.ctx.pop()

    @patch('app.routes.db.session.add')
    @patch('app.routes.db.session.commit')
    def test_register_user(self, mock_add, mock_commit):
        with self.client as client:
            response = client.post('/register', data={
                'username': 'testuser',
                'email': 'test@example.com',
                'password': 'password123',
                'confirm_password': 'password123'
            }, follow_redirects=True)
            
            # Check for flash message in session
            flashes = [msg for category, msg in session['_flashes']]
            self.assertIn('Congratulations, you are now a registered user!', flashes)

            mock_add.assert_called_once()
            mock_commit.assert_called_once()

if __name__ == '__main__':
    unittest.main()