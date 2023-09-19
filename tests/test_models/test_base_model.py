#!/usr/bin/python3
"""Module for testing base_model"""
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
from os import getenv


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                 'basemodel test not supported')
class test_basemodel(unittest.TestCase):
    """Class to test the BaseModel class"""

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """Setup method"""
        pass

    def tearDown(self):
        """Teardown method that deletes created file base"""
        try:
            os.remove('file.json')
        except Exception:
            pass

    def test_default(self):
        """Tests for BaseModel default attributes"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """Tests creating BaseModel from using kwargs"""
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """Tests creating BaseModel from using kwargs"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """Test __str__ method"""
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                         i.__dict__))

    def test_todict(self):
        """Test to_dict method"""
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """test kwargs none"""
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """test kwargs one"""
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertTrue(hasattr(new, 'Name'))
        self.assertEqual(new.Name, 'test')

    def test_id(self):
        """test id"""
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """test created_at"""
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """test updated_at"""
        new = self.value()
        # self.assertn(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        # self.assertFalse(new.created_at == new.updated_at)
