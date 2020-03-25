from app import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(45), nullable=False)
    author = db.Column(db.String(45), nullable=False)
    edition = db.Column(db.Integer, nullable=False)
    value = db.Column(db.Float)
    isbn = db.Column(db.String(20), nullable=False)
    listings = db.relationship('Listing', backref='book', lazy=True)

    def __init__(self, name, author, edition, value, isbn,
                 semester, major):
        self.name = name
        self.author = author
        self.edition = edition
        self.value = value
        self.isbn = isbn