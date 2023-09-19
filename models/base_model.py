#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from os import getenv
import models


db_mode = (getenv('HBNB_TYPE_STORAGE') == 'db')
if db_mode:
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if db_mode:
        id = Column(String(60), unique=True, nullable=False, primary_key=True)
        created_at = Column(
            DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(
            DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        for key, val in kwargs.items():
            if key == 'created_at' or key == 'updated_at':
                val = datetime.strptime(val, '%Y-%m-%dT%H:%M:%S.%f')
            if key != '__class__':
                setattr(self, key, val)

    def __str__(self):
        '''String representation of the object'''
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary

    def delete(self):
        models.storage.delete(self)
