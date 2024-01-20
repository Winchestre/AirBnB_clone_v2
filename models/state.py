#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all,delete", backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """Getter for cities related to this State"""
            from models import storage
            cities_list = []
            All_cities = storage.all(City)
            for city in All_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
