#!/usr/bin/python3
"""
Flask app
"""
from flask import Flask, jsonify, make_response
from routes.review_route import review_bp
from routes.resource_route import resource_bp
from routes.user_route import user_bp
from flask_cors import CORS
from flask_login import LoginManager
from models.user import User


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'f3d092628277affcb6761e4b94b354f31d17a52592f31333'
    login_manager = LoginManager(app)
    CORS(app)

    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(resource_bp)
    app.register_blueprint(review_bp)

    # Flask-Login configuration
    login_manager.login_view = 'user_bp.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.get(user_id)

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
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
