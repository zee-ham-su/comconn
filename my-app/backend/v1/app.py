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
    """
    Create and configure the Flask app.

    Returns:
        Flask: The configured Flask app.
    """
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'f3d092628277affcb6761e4b94b354f31d17a52592f31333'
    login_manager = LoginManager(app)
    CORS(app, methods=["POST"])

    # Register blueprints
    app.register_blueprint(user_bp)
    app.register_blueprint(resource_bp)
    app.register_blueprint(review_bp)

    # Flask-Login configuration
    login_manager.login_view = 'user_bp.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Root URL handler
    @app.route('/')
    def index():
        """
        Handle requests to the root URL.

        Returns:
        Response: JSON response with a welcome message.
        """
        return jsonify({'message': 'Welcome to the My App API'})

    # 404 Error handler
    @app.errorhandler(404)
    def not_found(error):
        """ 404 Error handler
        Parameters:
            error (Exception): the exception object
        Returns:
            responses: JSON response with a 404 error message.
        """
        return make_response(jsonify({'error': "Not found"}), 404)

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, threaded=True, debug=True)
