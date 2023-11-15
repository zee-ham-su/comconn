#!/usr/bin/python3
from models.storage.db_storage import DBStorage
import sys
sys.path.append("/root/commcon/my-app")

from flask import Blueprint, jsonify
from models.review import Review

review_bp = Blueprint('review_bp', __name__)


@review_bp.route('/reviews')
def get_reviews():
    storage = DBStorage()
    reviews = storage.get_all(Review)
    review_data = [{'id': review.id, 'user_id': review.user_id, 'resource_id': review.resource_id,
                    'rating': review.rating, 'comment': review.comment} for review in reviews]
    return jsonify({'reviews': review_data})
