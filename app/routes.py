# Imports the necessry modules for our Book model
from app import db
from app.models.book import Book
# Blueprint is a Flask class that provides a pattern for grouping related routes(endpoints)
from flask import Blueprint, jsonify, abort, make_response, request

# Instantiates a Blueprint instance
books_bp = Blueprint("books", __name__, url_prefix="/books")


def validate_book(book_id):
    try:
        book_id = int(book_id)
    except:
        abort(make_response({"message": f"book {book_id} invalid"}, 400))

    book = Book.query.get(book_id)

    if not book:
        abort(make_response({"message": f"book {book_id} not found"}, 404))

    return book

# Decorator that uses the books_bp Blueprint to define an endpoint and accepted HTTP method


@books_bp.route("", methods=["POST"])
def create_book():
    request_body = request.get_json()
    # Creates an instance of Book using the data in request_body
    new_book = Book(title=request_body["title"],
                    description=request_body["description"])
    db.session.add(new_book)
    db.session.commit()
    # make_response() function instantiates a Response object
    # the first parameter to make_response() is the HTTP response body.
    # defines the status code of the Response by passing an integer as the second argument to make_response(). When a second argument isn't specified, 200 is always the default value.
    return make_response(f"Book {new_book.title} successfully created", 201)


@books_bp.route("", methods=["GET"])
def read_all_books():
    books_response = []
    # Book.query.all() method returns a list of instances of Book
    books = Book.query.all()
    for book in books:
        books_response.append({
            "id": book.id,
            "title": book.title,
            "description": book.description
        })
    return jsonify(books_response), 200

# We are setting up a new route, so we must use the Blueprint decorator to define it
# book_id function parameter must match the route parameter in the decorator
# It will receive the part of the request path that lines up with the placeholder in the route


@books_bp.route("/<book_id>", methods=["GET"])
def read_one_book(book_id):
    # This is SQLAlchemy syntax to query for one Book resource
    # This method returns an instance of Book
    # The primary key of a book must be used here, book_id, which was provided as the route parameter
    book = validate_book(book_id)

    return {
        "id": book.id,
        "title": book.title,
        "description": book.description
    }


@books_bp.route("/<book_id>", methods=["PUT"])
def update_book(book_id):
    book = validate_book(book_id)

    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]

    db.session.commit()

    return make_response(f"Book #{book.id} successfully updated")


@books_bp.route("/<book_id>", methods=["DELETE"])
def delete_book(book_id):
    book = validate_book(book_id)

    db.session.delete(book)
    db.session.commit()

    return make_response(f"Book #{book.id} successfully deleted")

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
# # Instantiates a Blueprint
# books_bp = Blueprint("books", __name__, url_prefix="/books")
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
