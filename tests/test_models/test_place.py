#!/usr/bin/python3
"""Module to test Place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place


class test_Place(test_basemodel):
    """Class to test Place class"""

    def __init__(self, *args, **kwargs):
        """Initializes tests from BaseModel class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """test city_id attribute"""
        new = self.value()
        self.assertEqual(type(new.city_id), str)

    def test_user_id(self):
        """test user_id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_name(self):
        """test name attribute"""
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_description(self):
        """test description attribute"""
        new = self.value()
        self.assertEqual(type(new.description), str)

    def test_number_rooms(self):
        """test number_rooms attribute"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """test number_bathrooms attribute"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """test max_guest attribute"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """test price_by_night attribute"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """test latitude attribute"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_longitude(self):
        """test longitude attribute"""
        new = self.value()
        self.assertEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """test amenity_ids attribute"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)
