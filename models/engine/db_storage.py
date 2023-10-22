#!/usr/bin/python3
"""Module that defines class DBStorage. Handles the
    Object Relational Mapping (ORM)
"""

from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage:
    """Database storage engine for mysql storage"""
    __engine = None
    __session = None

    def __init__(self):
        '''dbstorage instance instantiation'''
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}".
                                      format(getenv("HBNB_MYSQL_USER"),
                                             getenv("HBNB_MYSQL_PWD"),
                                             getenv("HBNB_MYSQL_HOST"),
                                             getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)

        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current db session all cls objects
            this method must return a dictionary: (like FileStorage)
            key = <class-name>.<object-id>
            value = object
        """
        if cls is None:
            # Query all classes
            objs = self.__session.query(State).all()
            objs.extend(self.__session.query(City).all())
            objs.extend(self.__session.query(User).all())
            objs.extend(self.__session.query(Place).all())
            objs.extend(self.__session.query(Review).all())
            objs.extend(self.__session.query(Amenity).all())
        else:
            if type(cls) == str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
        return {"{}.{}".format(type(o).__name__, o.id): o for o in objs}

    def new(self, obj):
        """adds the obj to the current db session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes to the current db session"""
        self.__session.commit()

    def delete(self, obj=None):
        """deletes from the current database session the obj
            if it's not None
        """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads the database"""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """closes the working SQLAlchemy session"""
        self.__session.close()
