#!/usr/bin/env python3

from flask import Blueprint, jsonify, request, abort
from models.storage.db_storage import DBStorage
from models.resource_1 import Resource


storage = DBStorage()
resource_bp = Blueprint('resource_bp', __name__)


@resource_bp.route('/resources', methods=['GET'])
def get_resources():
    resources = storage.get_all(Resource)
    resource_data = [{'id': resource.id, 'name': resource.name,
                      'description': resource.description} for resource in resources]
    return jsonify({'resources': resource_data})


@resource_bp.route('/resources/<int:resource_id>', methods=['GET'])
def get_resource(resource_id):
    resource = storage.get(Resource, resource_id)
    if not resource:
        abort(404)
    return jsonify(resource.to_dict())


@resource_bp.route('/resources', methods=['POST'])
def create_resource():
    data = request.get_json()
    new_resource = Resource(**data)
    storage.new(new_resource)
    storage.save()
    return jsonify(new_resource.to_dict()), 201


@resource_bp.route('/resources/<int:resource_id>', methods=['PUT'])
def update_resource(resource_id):
    resource = storage.get(Resource, resource_id)
    if not resource:
        abort(404)
    data = request.get_json()
    for key, value in data.items():
        setattr(resource, key, value)
    storage.save()
    return jsonify(resource.to_dict())


@resource_bp.route('/resources/<int:resource_id>', methods=['DELETE'])
def delete_resource(resource_id):
    resource = storage.get(Resource, resource_id)
    if not resource:
        abort(404)
    storage.delete(resource)
    storage.save()
    return jsonify({}), 204


