from app import db

class Request(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    condition = db.Column(db.Integer, nullable=False)
    money = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __init__(self, condition, money, user_id, book_id):
        self.condition = condition
        self.money = money
        self.user_id = user_id
        self.book_id = book_id