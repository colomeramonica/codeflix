import unittest
from datetime import datetime
from category.domain.entities import Category
from dataclasses import dataclass, is_dataclass


class TestCategoryUnit(unittest.TestCase):

    def setUp(self):
        # Happy path
        self.valid_params_with_all_values = {
            'name': 'Movie',
            'description': 'some description',
            'is_active': True,
            'created_at': datetime.now()
        }

        self.valid_params_without_description = {
            'name': 'Movie',
            'is_active': True,
            'created_at': datetime.now()
        }

        self.valid_params_without_status = {
            'name': 'Movie',
            'description': 'some other description',
            'created_at': datetime.now()
        }

        self.valid_params_without_created = {
            'name': 'Movie',
            'description': 'some description again',
            'is_active': True
        }

        # Error cases
        self.error_params_empty_values = {}

        self.error_params_with_invalid_name = {
            'name': 123,
            'description': 'something',
            'is_active': True,
            'created_at': datetime.now()
        }

        self.error_params_with_invalid_description = {
            'name': 'Movie',
            'description': [],
            'is_active': True,
            'created_at': datetime.now()
        }

        self.error_params_with_invalid_status = {
            'name': 'Movie',
            'description': 'some description',
            'is_active': 'true',
            'created_at': datetime.now()
        }

        self.error_params_with_invalid_datetime = {
            'name': 'Movie',
            'description': 'some description',
            'is_active': True,
            'created_at': '23-10-22'
        }

    def test_is_valid_construct(self):
        self.assertTrue(is_dataclass(Category))

    def test_valid_construct_with_all_values(self):
        category = Category(**self.valid_params_with_all_values)

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'some description')
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

    def test_valid_construct_without_description(self):
        category = Category(**self.valid_params_without_description)

        self.assertEqual(category.name, 'Movie')
        self.assertIsNone(category.description)
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

    def test_valid_construct_without_status(self):
        category = Category(**self.valid_params_without_status)

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'some other description')
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

    def test_valid_construct_without_creation(self):
        category = Category(**self.valid_params_without_created)

        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'some description again')
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)

    def test_invalid_construct_with_empty_values(self):
        with self.assertRaises(TypeError):
            Category(**self.error_params_empty_values)

    def test_invalid_construct_with_invalid_name(self):
        print(Category(**self.error_params_with_invalid_name))
