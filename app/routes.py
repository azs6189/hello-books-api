# Blueprint is a Flask class that provides a pattern for grouping related routes(endpoints)
from flask import Blueprint, jsonify, abort, make_response

# ---------- Hardcoded Books data and two routes from the app commented out ----------
# class Book:
#     def __init__(self, id, title, description):
#         """Constructor with Book class attributes"""
#         self.id = id
#         self.title = title
#         self.description = description


# # Creates a list of Book instances
# books = [
#     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
#     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]


# Instantiates a Blueprint
books_bp = Blueprint("books", __name__, url_prefix="/books")

# ---------- GET /books and GET /books/<book_id> routes commented out ----------
# ---------- to be refactored to use in database ----------
# @books_bp.route("", methods=["GET"])
# def handle_books():
#     """Returns response body: list of books, in JSON format"""
#     books_response = []
#     for book in books:
#         books_response.append({
#             "id": book.id,
#             "title": book.title,
#             "description": book.description
#         })
#     # Returns and converts the list into an HTTP response body
#     return jsonify(books_response)


# @books_bp.route("/<book_id>", methods=["GET"])
# def validate_book(book_id):
#     """Validates book_id before returning a book description"""
#     try:
#         book_id = int(book_id)
#     except:
#         abort(make_response({"message": f"book {book_id} invalid"}, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     abort(make_response({"message": f"book {book_id} not found"}, 404))


# def handle_book(book_id):
#     """Returns response body: dictionary literal for one book with matching book_id"""
#     book = validate_book(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description
#     }
