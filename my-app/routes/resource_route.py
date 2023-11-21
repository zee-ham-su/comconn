#!/usr/bin/env python3

from flask import Blueprint, jsonify, request, abort
from models.storage.db_storage import DBStorage
from models.user import User
from models.review import Review
from models.resource_1 import Resource
from google_api import geocode_address

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


@resource_bp.route('/api/external/resources', methods=['GET'])
def external_resource_data():
    resources = storage.all(Resource).values()

    # Convert resource data to a format suitable for external clients
    formatted_resources = [
        {
            'name': resource.name,
            'type': resource.type,
            'location': resource.location,
            'description': resource.description
        }
        for resource in resources
    ]

    return jsonify(formatted_resources)


@resource_bp.route('/api/external/contributions', methods=['POST'])
def handle_external_contributions():
    # Ensure the request contains JSON data
    if not request.is_json:
        abort(400, description='Invalid JSON data')

    # Extract contribution data from the JSON request
    contribution_data = request.get_json()

    return jsonify({'message': 'Contribution received successfully'})


@resource_bp.route('/geocode', methods=['POST'])
def geocode():
    data = request.get_json()
    address = data.get('address')

    if not address:
        abort(400, description='Address not provided in the request.')

    geocoding_result = geocode_address(address)

    if geocoding_result:
        return jsonify(geocoding_result)
    else:
        abort(500, description='Error geocoding address.')
