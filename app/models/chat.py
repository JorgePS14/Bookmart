from app import db

class Chat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userchats = db.relationship('UserChat', backref='chat', lazy=True)
    messages = db.relationship('Message', backref='chat', lazy=True)

    def __init__(self):
        pass