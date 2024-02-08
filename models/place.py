#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
import models


place_amenity = Table("place_amenity", Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"),
            primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"),
            primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of rooms
        number_bathrooms: number of bathrooms
        max_guest: maximum number of guests
        price_by_night: price per night
        latitude: latitude
        longitude: longitude
        amenity_ids: list of amenity id
    """

    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship('Review',
                cascade="all, delete, delete-orphan", backref="place")
        amenities = relationship('Amenity', secondary=place_amenity,
                viewonly=False, back_populates='place_amenities')
 

    else:
        @property
        def reviews(self):
            """Getter for reviews related to this Place"""
            var = models.storage.all()
            reviews_list = []
            result = []
            for key in var:
                review = key.replace('.', ' ')
                review = shlex.split(review)
                if (review[0] == 'Review'):
                    reviews_list.append(var[key])
            for el in reviews_list:
                if el.place.id == self.id:
                    result.append(el)
            return result

        @property
        def amenities(self):
            """Returns list of amenity ids"""
            return self.amenity_ids

        @amenities.setter
        def amenities(self, obj=None):
            """Add an Amenity.id to the attribute amenity_ids"""
            if type(obj) is Amenity and obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)

        def __str__(self):
            """String representation of the Place instance"""
            return "[{}] ({}) {}".format(
                self.__class__.__name__,
                self.id,
                {
                    'id': self.id, 'created_at': self.created_at, 'updated_at': self.updated_at,
                    'number_bathrooms': self.number_bathrooms, 'longitude': self.longitude,
                    'city_id': self.city_id, 'user_id': self.user_id, 'latitude': self.latitude,
                    'price_by_night': self.price_by_night, 'name': self.name, 'max_guest': self.max_guest,
                    'number_rooms': self.number_rooms
                    }
                )
