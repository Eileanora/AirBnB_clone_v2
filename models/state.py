#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, db_mode
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if db_mode:
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        '''Initializes State'''
        super().__init__(*args, **kwargs)

    if not db_mode:
        @property
        def cities(self):
            '''
            Getter for cities that should return \
            the list of City instances with state_id \
            equals to the current State.id
            '''
            from models import storage
            from models.city import City
            results = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    results.append(city)
            return results
