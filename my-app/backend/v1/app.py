#!/usr/bin/python3
"""
Flask app
"""
from flask import Flask, jsonify, make_response
from routes.review_route import review_bp
from routes.resource_route import resource_bp
from routes.user_route import user_bp


def create_app():
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(resource_bp)
    app.register_blueprint(review_bp)

    # Root URL handler
    @app.route('/')
    def index():
        return jsonify({'message': 'Welcome to the My App API'})

    # 404 Error handler
    @app.errorhandler(404)
    def not_found(error):
        """ 404 Error
        ---
        responses:
            404:
                description: a resource was not found
        """
        return make_response(jsonify({'error': "Not found"}), 404)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)