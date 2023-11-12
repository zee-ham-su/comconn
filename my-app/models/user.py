#!/usr/bin/env python3
"""
Defines the User model for the Community Resource Mapping application.
"""

from sqlalchemy import Column, String

from found_model import BaseModel

class User(BaseModel):
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

    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    def __repr__(self):
        """
        Returns a string representation of the User instance.

        Returns:
            str: A string representation of the User instance.
        """
        return f"<User {self.id}: {self.username}>"
