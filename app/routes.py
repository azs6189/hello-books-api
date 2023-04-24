# Blueprint is a Flask class that provides a pattern for grouping related routes(endpoints)
from flask import Blueprint, jsonify


class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description


# Creates a list of Book instances
books = [
    Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
    Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
]

# Instantiates a Blueprint
books_bp = Blueprint("books", __name__, url_prefix="/books")


@books_bp.route("", methods=["GET"])
# Endpoint that will returns a response of list of books in JSON format
def handle_books():
    """Returns response body, list of books, in JSON format"""
    books_response = []
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response)
