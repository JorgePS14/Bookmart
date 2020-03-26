from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(45), unique=True, nullable=False)
    password = db.Column(db.String(45), nullable=False)
    username = db.Column(db.String(45), unique=True, nullable=False)
    location = db.Column(db.String(45))
    university = db.Column(db.String(45))
    semester = db.Column(db.Integer)
    major = db.Column(db.String(45))

    def __init__(self, email, password, username, location, university,
                 semester, major):
        self.email = email
        self.password = password
        self.username = username
        self.location = location
        self.university = university
        self.semester = semester
        self.major = major
