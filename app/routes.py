from flask import request, jsonify, Blueprint
from .models.user import User
from .models.listing import Listing
from app import db


user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route('/')
def index():
    return "<h1>Back end</h1>"

@user_blueprint.route('/api/user', methods=['GET','POST'])
def addUser():
    if request.method == "POST":
        user = User(
            request.form["email"],
            request.form["password"],
            request.form["username"],
            request.form["location"],
            request.form["university"],
            int(request.form["semester"]),
            request.form["major"]
        )
        db.session.add(user)
        db.session.commit()
        return '<h1>User added</h1>'
    return '<h1>API/User endpoint -- Try using Postman</h1>'

@user_blueprint.route('/api/book', methods=['GET','POST'])
def addBook():
    if request.method == "POST":
        book = Book(
            request.form["name"],
            request.form["author"],
            int(request.form["edition"]),
            float(request.form["value"]),
            request.form["isbn"]
        )
        db.session.add(book)
        db.session.commit()
        return '<h1>Book added</h1>'
    return '<h1>Add book endpoint -- Try using Postman</h1>'

@user_blueprint.route('/api/listing', methods=['GET','POST'])
def addListing():
    if request.method == "POST":
        photo = request.files["photo"]
        photo = photo.read()
        listing = Listing(
            photo,
            request.form["description"],
            int(request.form["condition"]),
            int(request.form["no_available"]),
            float(request.form["price"]),
            int(request.form["user_id"]),
            int(request.form["book_id"])
        )
        db.session.add(listing)
        db.session.commit()
        return '<h1>Listing added</h1>'
    return '<h1>Add listing endpoint -- Try using Postman</h1>'