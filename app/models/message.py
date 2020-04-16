from app import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(500), nullable=False)
    time = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable=False)

    def __init__(self, condition, money, user_id, book_id):
        self.condition = condition
        self.money = money
        self.user_id = user_id
        self.book_id = book_id