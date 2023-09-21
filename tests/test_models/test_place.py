#!/usr/bin/python3
""" Module to test place class"""
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import os


class test_Place(test_basemodel):
    """ place test class"""

    def __init__(self, *args, **kwargs):
        """ init the test class"""
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ test city id attr"""
        new = self.value()
        self.assertEqual(type(new.city_id), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_user_id(self):
        """ test user id attr"""
        new = self.value()
        self.assertEqual(type(new.user_id), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_name(self):
        """ test name attr"""
        new = self.value()
        self.assertEqual(type(new.name), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_description(self):
        """ test description attr"""
        new = self.value()
        self.assertEqual(type(new.description), str if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_number_rooms(self):
        """ test number rooms attr"""
        new = self.value()
        self.assertEqual(type(new.number_rooms), int if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_number_bathrooms(self):
        """ test number bathrooms attr"""
        new = self.value()
        self.assertEqual(type(new.number_bathrooms), int if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_max_guest(self):
        """ test max_guest attr"""
        new = self.value()
        self.assertEqual(type(new.max_guest), int if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_price_by_night(self):
        """ test price by night attr"""
        new = self.value()
        self.assertEqual(type(new.price_by_night), int if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_latitude(self):
        """ test latitude attr"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_longitude(self):
        """ test longitude attr"""
        new = self.value()
        self.assertEqual(type(new.latitude), float if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))

    def test_amenity_ids(self):
        """ test amenity ids attr"""
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list if
                os.getenv('HBNB_TYPE_STORAGE') != 'db' else
                type(None))
