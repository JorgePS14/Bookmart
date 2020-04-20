from app import db

class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #photo = db.Column(db.LargeBinary(2**32-1))
    photo = db.Column(db.String(200))
    description = db.Column(db.String(200), nullable=False)
    condition = db.Column(db.Integer, nullable=False)
    no_available = db.Column(db.Integer)
    price = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __init__(self, photo, description, condition, no_available, 
                price, user_id, book_id):
        self.photo = photo
        self.description = description
        self.condition = condition
        self.no_available = no_available
        self.price = price
        self.user_id = user_id
        self.book_id = book_id