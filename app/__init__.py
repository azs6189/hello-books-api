# This is the starting, boilerplate code to start a Flask application
from flask import Flask

# Imports and sets up the packages SQLAlchemy and Migrate (a companion package to SQLAlchemy)
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from dotenv import load_dotenv

# This built-in module provides a way to read environment variables
import os

# Sets up db and migrate, which are conventional variables that give us access to database operations
db = SQLAlchemy()
migrate = Migrate()

# This package imports the load_dotenv() method which loads the values from the .env file so that the os module is able to see them
load_dotenv()


def create_app(test_config=None):
    """Starting boilerplate code to start a Flask application and configure the database to use SQLAlchemy"""
    app = Flask(__name__)

    if not test_config:
        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")
    # Configures the app to include two new SQLAlchemy settings
    # This config is set to False to hide a warning about a feature in SQLAlchemy that will not be used
    # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # # This config is set to the connection string for our database, hello_books_development
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    # Import models here
    from app.models.book import Book
    from app.models.author import Author

    # Initializes Flask-Migrate extension using the init_app method to connect db and migrate to our Flask app
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from .book_routes import books_bp
    app.register_blueprint(books_bp)
    from .author_routes import authors_bp
    app.register_blueprint(authors_bp)

    return app
