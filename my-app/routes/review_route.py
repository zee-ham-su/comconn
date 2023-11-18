#!/usr/bin/env python3

from flask import Blueprint, jsonify, request, abort
from models.storage.db_storage import DBStorage
from models.review import Review

review_bp = Blueprint('review_bp', __name__)


def get_storage():
    return DBStorage()


@review_bp.route('/reviews', methods=['GET'])
def get_reviews():
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
    storage = get_storage()
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@review_bp.route('/reviews', methods=['POST'])
def create_review():
    storage = get_storage()
    data = request.get_json()
    new_review = Review(**data)
    storage.new(new_review)
    storage.save()
    return jsonify(new_review.to_dict()), 201


@review_bp.route('/reviews/<int:review_id>', methods=['PUT'])
def update_review(review_id):
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
    storage = get_storage()
    review = storage.get(Review, review_id)
    if not review:
        abort(404)
    storage.delete(review)
    storage.save()
    return jsonify({}), 204
