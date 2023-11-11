#!/usr/bin/python3
"""
Flask app
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify

app = Flask(__name__)
# Update with your desired database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

@app.route('/api/hello', methods=['GET'])
def hello():
    return jsonify(message='Hello from Flask!')


if __name__ == "__main__":
    app.run(debug=True)
