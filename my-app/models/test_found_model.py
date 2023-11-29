import unittest
from datetime import datetime
from found_model import BaseModel

class BaseModelTestCase(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_base_model_attributes(self):
        self.assertIsNone(self.base_model.id)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_base_model_save(self):
        self.base_model.save()
        self.assertIsNotNone(self.base_model.id)

    def test_base_model_delete(self):
        self.base_model.save()
        self.base_model.delete()
        self.assertIsNone(self.base_model.id)

    def test_base_model_create(self):
        instance = BaseModel.create()
        self.assertIsNotNone(instance.id)

    def test_base_model_retrieve(self):
        instance = BaseModel.create()
        retrieved_instance = BaseModel.retrieve(instance.id)
        self.assertEqual(retrieved_instance, instance)

    def test_base_model_count(self):
        initial_count = BaseModel.count()
        instance = BaseModel.create()
        updated_count = BaseModel.count()
        self.assertEqual(updated_count, initial_count + 1)

    def test_base_model_update_attributes(self):
        self.base_model.update_attributes(created_at=datetime(2022, 1, 1))
        self.assertEqual(self.base_model.created_at, datetime(2022, 1, 1))

if __name__ == '__main__':
    unittest.main()