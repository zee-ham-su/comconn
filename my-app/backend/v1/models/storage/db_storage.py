#!/usr/bin/env python
"""
backend/db_storage.py

Defines the DBStorage class for interacting with the MySQL database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.found_model import Base
from models import *
from config import AppConfig

class DBStorage:
    """
    Interacts with the MySQL database.

    Attributes:
        __engine: The SQLAlchemy engine for database interaction.
        __session: The SQLAlchemy session for database transactions.

    Methods:
        __init__(): Initializes a DBStorage object.
        all(cls=None): Query on the current database session.
        new(obj): Adds the object to the current database session.
        save(): Commits all changes of the current database session.
        delete(obj=None): Deletes from the current database session obj if not None.
        reload(): Reloads data from the database.
        close(): Calls remove() method on the private session attribute.
        get(cls, id): Returns the object based on the class name and its ID, or None if not found.
        count(cls=None): Count the number of objects in storage.
    """

    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes a DBStorage object.
        """
        self.config = AppConfig()
        self.__engine = create_engine(
            f'mysql+mysqldb://{self.config.MYAPP_DB_USER}:{self.config.MYAPP_DB_PWD}@{self.config.MYAPP_DB_HOST}/{self.config.MYAPP_DB_NAME}'
        )
        if self.config.MYAPP_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        Query on the current database session.
        """
        query_classes = classes.values() if cls is None else [cls]
        new_dict = {}

        for cls_to_query in query_classes:
            objs = self.__session.query(cls_to_query).all()
            new_dict.update({f"{obj.__class__.__name__}.{obj.id}": obj for obj in objs})

        return new_dict

    def new(self, obj):
        """
        Adds the object to the current database session.
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session.
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes from the current database session obj if not None.
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Reloads data from the database.
        """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """
        Calls remove() method on the private session attribute.
        """
        with self.__session() as session:
            pass

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or None if not found.
        """
        if cls not in classes.values():
            return None

        all_cls = self.all(cls)
        return next((value for value in all_cls.values() if value.id == id), None)

    def count(self, cls=None):
        """
        Count the number of objects in storage.
        """
        all_class = classes.values() if not cls else [cls]
        return sum(len(self.all(clas).values()) for clas in all_class)
