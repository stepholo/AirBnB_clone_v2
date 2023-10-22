#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""

import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage.
        If cls is provided, returns a dictionary filtered by class type."""
        if cls is not None:
            if type(cls) == str:
                cls = eval(cls)
            filtered_objs = {}
            for key, obj in self.__objects.items():
                if type(obj) == cls:
                    filtered_objs[key] = obj
            return filtered_objs
        return self.__objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """Saves storage dictionary to file"""
        di_ct = {o: self.__objects[o].to_dict() for o in self.__objects.keys()}
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            json.dump(di_ct, f)

    def reload(self):
        """Loads storage dictionary from file"""
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as f:
                for j in json.load(f).values():
                    name = j["__class__"]
                    del j["__class__"]
                    self.new(eval(name)(**j))
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """deletes the object obj from the attribute
            __objects if its's inside it
        """
        try:
            del self.__objects["{}.{}".format(type(obj).__name__, obj.id)]
        except (AttributeError, KeyError):
            pass

    def close(self):
        """call the reload method."""
        self.reload()
