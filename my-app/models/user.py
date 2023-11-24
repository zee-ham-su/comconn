#!/usr/bin/env python3
"""
Defines the User model for the Community Resource Mapping application.
"""
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from sqlalchemy import Column, String, Integer, DateTime
from models.found_model import BaseModel, Base
from datetime import datetime
import secrets
from sqlalchemy.orm import relationship


def generate_unique_salt():
    """
    Generate a unique salt using the secrets module.

    Returns:
        str: A random 8-character hexadecimal string used for salting passwords.
    """
    return secrets.token_hex(8)


class User(BaseModel, Base, UserMixin):
    """
    User model for representing users in the application.

    Attributes:
        username (str): The username of the user.
        email (str): The email address of the user.
        password_hash (str): The password of the user.
        unique_salt (str): The unique salt for the user.

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
    unique_salt = Column(String(255))
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
        self.unique_salt = generate_unique_salt()
        self.password_hash = generate_password_hash(
            self.unique_salt + password)

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
        return check_password_hash(self.password_hash, self.unique_salt + password)

    def get_id(self):
        """
        Returns the user ID, required for Flask-Login.

        Returns:
            str: The user ID.
        """
        return str(self.id)
