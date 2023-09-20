#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an Amenity for a MYSQL database.

    Inherits from SQLAlchemy Base and links to the MYSQL table amenities.

    Attributes:
    __tablename__(str): The name of the MySQL table to store Amenities.
    name (sqlalchemy String): The amenity name.
    place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    if models.storage_t == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Initialize Amenity"""
        super().__init__(*args, **kwargs)
