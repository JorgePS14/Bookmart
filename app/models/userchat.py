from app import db

class UserChat(db.Model):
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('user.id'), 
                        primary_key = True, 
                        nullable=False,
                        autoincrement = False)
    chat_id = db.Column(db.Integer, 
                        db.ForeignKey('chat.id'), 
                        primary_key = True,
                        nullable=False,
                        autoincrement = False)

    def __init__(self, user_id, chat_id):
        self.user_id = user_id
        self.chat_id = chat_id