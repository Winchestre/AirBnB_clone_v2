#!/usr/bin/python3
"""This module defines a class to manage database storage for hbnb"""
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiates database engine"""
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host_name = getenv('HBNB_MYSQL_HOST')
        db_name = getenv('HBNB_MYSQL_DB')
        db_url = f'mysql+mysqldb://{user}:{password}@{host_name}/{db_name}'

        self.__engine = create_engine(db_url, pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls-None):
        """Query on the current database session (self.__session)
        all objects depending on the class name
        """
        all_cls_dict = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            result = self.__session.query(cls)
            for obj in result:
                key = f'{type(obj).__name__}.{obj.id}'
                all_cls_dict[key] = obj
        else:
            classes = [State, City, User, Place, Review, Amenity]
            for clas in classes:
                result = self.__session.query(clas)
                for obj in result:
                    key = f'{type(obj).__name__}.{obj.id}'
                    all_cls_dict[key] = obj

        return all_cls_dict

    def new(self, obj):
        """Add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables in the database and the current session"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
        self.__session = Session()

    def close(self):
        """Remove session"""
        self.__session.close()
