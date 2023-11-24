#!/usr/bin/env python3
"""
Defines the User model for the Community Resource Mapping application.
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, DateTime
from models.found_model import BaseModel, Base
from datetime import datetime
import sys
from sqlalchemy.orm import relationship
sys.path.append("/root/commcon/my-app")


class User(BaseModel, Base, UserMixin):
    """
    User model for representing users in the application.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        password_hash (str): The password of the user.

    Methods:
        __repr__: Returns a string representation of the User instance.
        to_dict: Returns a dictionary representation of the User instance.
        set_password: Sets the password for the user.
        check_password: Checks if the provided password matches the user's password.
    """
    __tablename__ = "users"

    username = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
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
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def set_password(self, password):
        """
        Sets the password for the user.

        Args:
            password (str): The password to set.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Checks if the provided password matches the user's password.

        Args:
            password (str): The password to check.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        if self.password_hash is None:
            return False
        return check_password_hash(self.password_hash, password)
    
    def get_id(self):
        """
        Returns the user ID, required for Flask-Login.

        Returns:
            str: The user ID.
        """
        return str(self.id)
