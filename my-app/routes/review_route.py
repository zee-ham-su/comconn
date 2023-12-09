#!/usr/bin/env python3

from flask import Blueprint, jsonify, request, abort
from models.storage.db_storage import DBStorage
from models.review import Review

review_bp = Blueprint('review_bp', __name__)


def get_storage():
    """
    Get an instance of the storage system.

    Returns:
        DBStorage: An instance of the database storage system.
    """
    return DBStorage()


@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
    """
    Retrieve a list of all reviews.

    Returns:
        Response: JSON response with a list of reviews.
    """
    storage = get_storage()
    reviews = storage.get_all(Review)
    review_data = [{'id': review.id, 'user_id': review.user_id,
                    'resource_id': review.resource_id,
                    'rating': review.rating, 'comment': review.comment,
                    'created_at': review.created_at,
                    'updated_at': review.updated_at} for review in reviews]
    return jsonify({'reviews': review_data})


@review_bp.route('/reviews/<int:review_id>', methods=['GET'])
def get_review(review_id):
    """
    Retrieve information about a specific review.

    Parameters:
        review_id (int): The ID of the review to retrieve.

    Returns:
        Response: JSON response with information about the requested review.
    """
    storage = get_storage()
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@review_bp.route('/reviews', methods=['POST'])
def create_review():
    """
    Create a new review.

    Returns:
        Response: JSON response with information about the newly created review.
    """
    storage = get_storage()
    data = request.get_json()
    new_review = Review(**data)
    storage.new(new_review)
    storage.save()
    return jsonify(new_review.to_dict()), 201


@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
    """
    Update information about a specific review.

    Parameters:
        review_id (int): The ID of the review to update.

    Returns:
        Response: JSON response with updated information about the review.
    """
    storage = get_storage()
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    data = request.get_json()
    for key, value in data.items():
        setattr(review, key, value)
    storage.save()
    return jsonify(review.to_dict())


@review_bp.route('/reviews/<int:review_id>', methods=['DELETE'])
def delete_review(review_id):
    """
    Delete a specific review.

    Parameters:
        review_id (int): The ID of the review to delete.

    Returns:
        Response: JSON response indicating a successful deletion.
    """
    storage = get_storage()
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 204
