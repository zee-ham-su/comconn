import unittest
from datetime import datetime
from user import User

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user = User(username='john_doe', email='john@example.com')
        self.user.set_password('password')

    def test_user_attributes(self):
        self.assertEqual(self.user.username, 'john_doe')
        self.assertEqual(self.user.email, 'john@example.com')
        self.assertIsNotNone(self.user.password_hash)
        self.assertIsNotNone(self.user.unique_salt)
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_user_repr(self):
        expected_repr = "<User None: john_doe>"
        self.assertEqual(repr(self.user), expected_repr)

    def test_user_to_dict(self):
        expected_dict = {
            'id': None,
            'username': 'john_doe',
            'email': 'john@example.com',
            'created_at': self.user.created_at,
            'updated_at': self.user.updated_at
        }
        self.assertEqual(self.user.to_dict(), expected_dict)

    def test_check_password(self):
        self.assertTrue(self.user.check_password('password'))
        self.assertFalse(self.user.check_password('wrong_password'))

    def test_get_id(self):
        self.assertIsNone(self.user.get_id())

if __name__ == '__main__':
    unittest.main()