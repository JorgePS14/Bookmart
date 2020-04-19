from flask import request, jsonify, Blueprint
from .models.user import User
from .models.book import Book
from .models.listing import Listing
# from flask_jwt import jwt_required, current_identity
from app import db

user_blueprint = Blueprint("user_blueprint", __name__)
book_blueprint = Blueprint("book_blueprint", __name__)
listing_blueprint = Blueprint("listing_blueprint", __name__)



@user_blueprint.route('/api/user', methods=['GET', 'POST'])
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
        return 'OK', 200

    message = {'Endpoint': 'Add User',
               'Description': 'Used to register user in db'}
    return jsonify(message)


@book_blueprint.route('/api/book', methods=['GET', 'POST'])
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
        return 'OK', 200

    message = {'Endpoint': 'Add Book',
               'Description': 'Used to register book in db'}
    return jsonify(message)


@listing_blueprint.route('/api/listing', methods=['GET', 'POST'])
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
        return 'OK', 200

    message = {'Endpoint': 'Add Listing',
               'Description': 'Used to register listing in db'}
    return jsonify(message)
