#!/usr/bin/python3
'''Module defining the DBStorage class'''
from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        '''Initialize a DBStorage instance'''
        self.engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            getenv('HBNB_MYSQL_USER'),
            getenv('HBNB_MYSQL_PWD'),
            getenv('HBNB_MYSQL_HOST'),
            getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)
        if getenv('HNBN_ENV' == 'test'):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''Query on the current database session\
         and return a dictionary of all objects of\
         a specific class
        '''
        objects = {}
        if cls:
            results = self.__session.query(cls).all()
            for result in results:
                objects[result.__class__.__name__ + '.' + result.id] = result
        return objects

    def new(self, obj):
        '''Add a new object to the current database session'''
        self.__session.add(obj)

    def save(self):
        '''Commit all changes of the current database session'''
        self.__session.commit()

    def delete(self, obj=None):
        '''Delete from the current database session obj if not None'''
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        '''Create all tables in the database and\
         create the current database session
        '''
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Base.metadata.create_all(self.__engine)
        self.__session = scoped_session(Session)
