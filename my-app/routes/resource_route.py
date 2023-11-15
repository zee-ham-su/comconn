#!/usr/bin/python3
from models.storage.db_storage import DBStorage
import sys
sys.path.append("/root/commcon/my-app")

from flask import Blueprint, jsonify
from models.resource_1 import Resource
resource_bp = Blueprint('resource_bp', __name__)


@resource_bp.route('/resources')
def get_resources():
    storage = DBStorage()
    resources = storage.get_all(Resource)
    resource_data = [{'id': resource.id, 'name': resource.name,
                      'category': resource.category} for resource in resources]
    return jsonify({'resources': resource_data})
