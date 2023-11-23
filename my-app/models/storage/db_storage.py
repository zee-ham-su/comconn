#!/usr/bin/env python
"""
backend/db_storage.py
Defines the DBStorage class for interacting with the MySQL database.
"""
import sys
sys.path.append("/root/commcon/my-app")

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, Session
from models.user import User
from models.review import Review
from models.found_model import BaseModel, Base
from models.resource_1 import Resource
from models.storage.config import AppConfig


classes = {"User": User, "Review": Review, "Resource": Resource}


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

    @property
    def engine(self):
        """Property to access the engine."""
        return self.__engine
    
    def __init__(self):
        """
        Initializes a DBStorage object.
        """
        self.config = AppConfig()
        self.__engine = create_engine(
            f'mysql+mysqldb://{self.config.MYAPP_DB_USER}:{self.config.MYAPP_DB_PWD}@{self.config.MYAPP_DB_HOST}/{self.config.MYAPP_DB_NAME}',
            pool_pre_ping=True 
        )

        if self.config.MYAPP_ENV == "test":
            Base.metadata.drop_all(self.__engine)
        self.reload()

    def all(self, cls=None):
        """
        Query on the current database session.
        """
        query_classes = classes.values() if cls is None else [cls]
        new_dict = {}

        for cls_to_query in query_classes:
            objs = self.__session.query(cls_to_query).all()
            new_dict.update(
                {f"{obj.__class__.__name__}.{obj.id}": obj for obj in objs})

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
        if self.__session:
            self.__session.remove()

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
    
    def get_all(self, model):
        """
        Returns a list of all objects of the given model.
        """
        return self.__session.query(model).all()
    
    def create_session(self):
        """
        Creates a new session if it doesn't exist, otherwise returns the existing session.
        """
        if not self.__engine:
            self.__engine = create_engine(
                f'mysql+mysqldb://{self.config.MYAPP_DB_USER}:{self.config.MYAPP_DB_PWD}@{self.config.MYAPP_DB_HOST}/{self.config.MYAPP_DB_NAME}',
                pool_pre_ping=True
            )

        if not self.__session:
            sess_factory = sessionmaker(
                bind=self.__engine, expire_on_commit=False)
            Session = scoped_session(sess_factory)
            self.__session = Session

        return self.__session
    
    def get_user_by_username(self, username):
        """
        Get a user by username.

        Args:
            username (str): The username to search for.

        Returns:
            User or None: The User object if found, None otherwise.
        """
        return self.__session.query(User).filter_by(username=username).first()
    
    
    def get_user_by_email(self, email):
        """
        Get a user by email.

        Args:
            email (str): The email to search for.

        Returns:
            User or None: The User object if found, None otherwise.
        """
        return self.__session.query(User).filter_by(email=email).first()
