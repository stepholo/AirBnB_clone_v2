#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """ State class / table model"""

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship(
            "City", backref="state", 
            cascade="all, delete, delete-orphan")
    
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """returns list of city instances with state_id
                equals the current State.id
                FileStorage relationship between State and City
            """
            from models import storage
            cities_rel = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    cities_rel.append(city)
            return cites_rel
