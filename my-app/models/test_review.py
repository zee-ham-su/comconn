import unittest
from datetime import datetime
from review import Review

class ReviewTestCase(unittest.TestCase):
    def setUp(self):
        self.review = Review(user_id=1, resource_id=1, rating=5, comment='Great resource')

    def test_review_attributes(self):
        self.assertEqual(self.review.user_id, 1)
        self.assertEqual(self.review.resource_id, 1)
        self.assertEqual(self.review.rating, 5)
        self.assertEqual(self.review.comment, 'Great resource')
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_review_to_dict(self):
        expected_dict = {
            'id': None,
            'user_id': 1,
            'resource_id': 1,
            'rating': 5,
            'comment': 'Great resource',
            'created_at': self.review.created_at,
            'updated_at': self.review.updated_at
        }
        self.assertEqual(self.review.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()