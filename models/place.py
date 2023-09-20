#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import models
from os import getenv

class Place(BaseModel, Base):
    """ A place to stay """

    __tablename__ = 'places'
    

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    reviews = relationship(
            'Review', backref='place',
            cascade='all, delete, delete-orphan')

    amenity_ids = []

    if getenv("HBNB_TYPE_STOREAGE", None) != "db":
        @property
        def reviews(self):
            """returns list of reviews instances wiht place_id
                equals to the current place.id
                FileStorage relationship between Place and Review
            """
            lst = []
            for rev in list(models.storage.all(Review).values()):
                if rev.place_id == self.id:
                    lst.append(rev)
            return lst
