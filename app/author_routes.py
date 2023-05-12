from app import db

from app.models.author import Author

from flask import Blueprint, jsonify, abort, make_response, request

# Instantiates a Blueprint instance
authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")
