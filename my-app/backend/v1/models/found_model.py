#!/usr/bin/env python3
"""
backend/models/basemodel.py

This module defines the BaseModel class, which serves as the foundation for other models.
"""

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModel(db.Model):
    """
    BaseModel class serves as the base model for other models.

    Attributes:
        id (int): Primary key.
        created_at (DateTime): Timestamp of creation.
        updated_at (DateTime): Timestamp of the last update.

    Methods:
        __init__: Initialization of the base model.
        save: Save the instance to the database.
        delete: Delete the instance from the database.
        create: Create a new instance and save it to the database.
        retrieve: Retrieve an instance by its primary key.
        count: Get the total count of instances.
        update_attributes: Update instance attributes and save to the database.
    """

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __init__(self, *args, **kwargs):
	    """Initialization of the base model"""
        super().__init__(*args, **kwargs)

    def save(self):
	    """Commits the instance to the database."""
        db.session.add(self)
        db.session.commit()

    def delete(self):
	    """Deletes the instance from the database."""										
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def create(cls, **kwargs):
	    """
        Creates and saves a new instance.

        Args:
            **kwargs: Keyword arguments for initializing the instance.

        Returns:
            instance: The newly created instance.
        """
        instance = cls(**kwargs)
        instance.save()
        return instance

    @classmethod
    def retrieve(cls, object_id):
	    """
        Retrieves an instance by its primary key.

        Args:
            object_id: Primary key of the instance to retrieve.

        Returns:
            instance: The retrieved instance.
        """
        return cls.query.get(object_id)

    @classmethod
    def count(cls):
	    """
        Returns the total count of instances.

        Returns:
            int: Total count of instances.
        """
        return cls.query.count()

    def update_attributes(self, **kwargs):
	    """
        Updates instance attributes and saves to the database.

        Args:
            **kwargs: Keyword arguments for updating instance attributes.
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
	