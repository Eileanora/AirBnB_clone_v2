#!/usr/bin/python3
"""Module to test City class"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City


class test_City(test_basemodel):
    """Class to test City class"""

    def __init__(self, *args, **kwargs):
        """Initializes tests from BaseModel class"""
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """test state_id attribute"""
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    def test_name(self):
        """test name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
