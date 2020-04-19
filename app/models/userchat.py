from app import db

class UserChat(db.Model):
    buyer_id = db.Column(db.Integer, 
                        db.ForeignKey('user.id'), 
                        primary_key = True, 
                        nullable=False,
                        autoincrement = False)
    buyer_id = db.Column(db.Integer, 
                        db.ForeignKey('user.id'), 
                        primary_key = True, 
                        nullable=False,
                        autoincrement = False)
    chat_id = db.Column(db.Integer, 
                        db.ForeignKey('chat.id'), 
                        primary_key = True,
                        nullable=False,
                        autoincrement = False)

    def __init__(self, buyer_id, seller_id, chat_id):
        self.buyer_id = buyer_id
        self.seller_id = seller_id
        self.chat_id = chat_id