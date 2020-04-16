from app import db

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, condition, money, user_id, book_id):
        print("Chat created.")