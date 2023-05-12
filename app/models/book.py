from app import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    # establishes the one-to-many relationship
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"))
    author = db.relationship("Author", back_populates="books")

    def to_dict(self):
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description

        return book_as_dict

    @classmethod
    def from_dict(cls, book_data):
        """Takes in a dictionary and returns a new Book instance"""
        new_book = Book(title=book_data["title"],
                        description=book_data["description"])
        return new_book
