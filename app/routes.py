# Blueprint is a Flask class that provides a pattern for grouping related routes(endpoints)
from flask import Blueprint


class Book:
    def __init__(self, id, title, description):
        self.id = id
        self.title = title
        self.description = description


books = [
    Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
    Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
    Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
]

books_bp = Blueprint("books", __name__, url_prefix="/books")
