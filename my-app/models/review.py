#!/usr/bin/env python3
"""
Defines the Review model for the Community Resource Mapping application.
"""

from models.found_model import BaseModel
from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """
    Review model for representing reviews in the application.

    Attributes:
        user_id (int): The ID of the user who created the review.
        resource_id (int): The ID of the resource being reviewed.
        rating (int): The rating given in the review.
        comment (str): The comment provided in the review.

    Relationships:
        user: Relationship with the User model.
        resource: Relationship with the Resource model.

    Methods:
        None
    """
    __tablename__ = "reviews"

    user_id = Column(Integer, ForeignKey('users.id'))
    resource_id = Column(Integer, ForeignKey('resources.id'))
    rating = Column(Integer)
    comment = Column(Text)

    user = relationship("User", back_populates="reviews")
    resource = relationship("Resource", back_populates="reviews")
