# app/models/author.py
from app import db


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    # establishes the one-to-many relationship
    books = db.relationship("Book", back_populates="author")
