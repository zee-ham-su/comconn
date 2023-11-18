#!/usr/bin/env python3
"""
Defines the User model for the Community Resource Mapping application.
"""
from sqlalchemy import Column, String, Integer, DateTime
from models.found_model import BaseModel, Base
from datetime import datetime
import sys
sys.path.append("/root/commcon/my-app")

from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """
    User model for representing users in the application.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        password (str): The password of the user.

    Methods:
        __repr__: Returns a string representation of the User instance.
    """
    __tablename__ = "users"

    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow)

    reviews = relationship("Review", back_populates="user",
                           cascade="all, delete-orphan")

    def __repr__(self):
        """
        Returns a string representation of the User instance.

        Returns:
            str: A string representation of the User instance.
        """
        return f"<User {self.id}: {self.username}>"
    
    def to_dict(self):
        """
        Returns a dictionary representation of the User instance.

        Returns:
            dict: A dictionary containing user information.
        """
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'password': self.password,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
