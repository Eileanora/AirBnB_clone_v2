#!/usr/bin/python3
"""Module to test Review class"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review


class test_review(test_basemodel):
    """Class to test Review class"""

    def __init__(self, *args, **kwargs):
        """Initializes tests from BaseModel class"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """test place_id attribute"""
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        """test user_id attribute"""
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    def test_text(self):
        """test text attribute"""
        new = self.value()
        self.assertEqual(type(new.text), str)
