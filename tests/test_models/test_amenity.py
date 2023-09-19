#!/usr/bin/python3
"""Module to test Amenity class"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity


class test_Amenity(test_basemodel):
    """Class to test Amenity class"""

    def __init__(self, *args, **kwargs):
        """Initializes tests from BaseModel class"""
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """Tests name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)
