#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import shlex


class State(BaseModel, Base):
    """ State class
    Attributes:
        name: name input
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete, delete-orphan",
            backref="state")

    @property
    def cities(self):
        """Getter for cities related to this State"""
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if city[0] == 'City':
                lista.append(var[key])
        for el in lista:
            if el.state_id == self.id:
                result.append(el)
        return result
