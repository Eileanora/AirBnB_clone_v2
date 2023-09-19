#!/usr/bin/python3
"""Module to test State class"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """Class to test State class"""

    def __init__(self, *args, **kwargs):
        """Initializes tests from BaseModel class"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """Tests name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
