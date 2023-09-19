#!/usr/bin/python3
"""Module to test User class"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User


class test_User(test_basemodel):
    """Class to test User class"""
    def __init__(self, *args, **kwargs):
        """Initializes tests from BaseModel class"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """test first_name attribute"""
        new = self.value()
        self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        """test last_name attribute"""
        new = self.value()
        self.assertEqual(type(new.last_name), str)

    def test_email(self):
        """test email attribute"""
        new = self.value()
        self.assertEqual(type(new.email), str)

    def test_password(self):
        """test password attribute"""
        new = self.value()
        self.assertEqual(type(new.password), str)
