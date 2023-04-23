# This is the starting, boilerplate code to start a Flask application
from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__)

    return app
