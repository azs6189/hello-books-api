from app import db

from app.models.author import Author

from flask import Blueprint, jsonify, abort, make_response, request

# Instantiates a Blueprint instance
authors_bp = Blueprint("authors_bp", __name__, url_prefix="/authors")


@authors_bp.route("", methods=["POST"])
def create_author():
    request_body = request.get_json()
    new_author = Author(name=request_body["name"],)

    db.session.add(new_author)
    db.session.commit()

    return make_response(jsonify(f"Author {new_author.name} successfully created"), 201)