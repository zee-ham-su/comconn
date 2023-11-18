#!/usr/bin/env python3
"""
Defines the Review model for the Community Resource Mapping application.
"""
from datetime import datetime
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from models.found_model import BaseModel, Base
import sys
sys.path.append("/root/commcon/my-app")


class Review(BaseModel, Base):
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

    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    resource_id = Column(Integer, ForeignKey('resources.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    user = relationship("User", back_populates="reviews")
    resource = relationship("Resource", back_populates="reviews")


    def to_dict(self):
        """
        Returns a dictionary representation of the Review instance.

        Returns:
            dict: A dictionary representation of the Review instance.
        """
        return {
            'id': self.id,
            'user_id': self.user_id,
            'resource_id': self.resource_id,
            'rating': self.rating,
            'comment': self.comment,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
