from app import db
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)
    location = db.Column(db.String(45))
    university = db.Column(db.String(45))
    semester = db.Column(db.Integer)
    major = db.Column(db.String(45))
    listings = db.relationship('Listing', backref='user', lazy=True)
    requests = db.relationship('Request', backref='user', lazy=True)
    #chats = db.relationship('UserChat', backref='user', lazy=True) //Not needed for now

    def __init__(self, email, username, location, university,
                 semester, major):
        self.email = email
        self.username = username
        self.location = location
        self.university = university
        self.semester = semester
        self.major = major

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
