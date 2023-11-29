import unittest
from datetime import datetime
from resource_1 import Resource

class ResourceTestCase(unittest.TestCase):
    def setUp(self):
        self.resource = Resource(id=1, name='Hospital', description='A medical facility')

    def test_resource_attributes(self):
        self.assertEqual(self.resource.id, 1)
        self.assertEqual(self.resource.name, 'Hospital')
        self.assertEqual(self.resource.description, 'A medical facility')
        self.assertIsInstance(self.resource.created_at, datetime)
        self.assertIsInstance(self.resource.updated_at, datetime)

    def test_resource_to_dict(self):
        expected_dict = {
            'id': 1,
            'name': 'Hospital',
            'description': 'A medical facility',
            'created_at': self.resource.created_at,
            'updated_at': self.resource.updated_at
        }
        self.assertEqual(self.resource.to_dict(), expected_dict)

    def test_resource_repr(self):
        expected_repr = "<Resource 1: Hospital>"
        self.assertEqual(repr(self.resource), expected_repr)

if __name__ == '__main__':
    unittest.main()