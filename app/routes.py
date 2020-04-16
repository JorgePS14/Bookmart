from flask import request, jsonify, Blueprint
from .models.user import User
from .models.book import Book
from .models.request import Request
from .models.listing import Listing
from app import db

user_blueprint = Blueprint("user_blueprint", __name__)
book_blueprint = Blueprint("book_blueprint", __name__)
listing_blueprint = Blueprint("listing_blueprint", __name__)
request_blueprint = Blueprint("request_blueprint", __name__)

@user_blueprint.route('/')
def index():
    return "<h1>Back end</h1>"

@user_blueprint.route('/api/user', methods=['GET','POST'])
def addUser():
    if request.method == "POST":
        user_data = request.get_json()
        user = User(
            user_data["email"],
            user_data["password"],
            user_data["username"],
            user_data["location"],
            user_data["university"],
            user_data["semester"],
            user_data["major"]
        )
        db.session.add(user)
        db.session.commit()
        return 'OK', 200
    
    message = {'Endpoint' : 'Add User',
                'Description' : 'Used to register user in db'}
    return jsonify(message)

@book_blueprint.route('/api/book', methods=['GET','POST'])
def addBook():
    if request.method == "POST":
        book_data = request.get_json()
        book = Book(
            book_data["name"],
            book_data["author"],
            int(book_data["edition"]),
            float(book_data["value"]),
            book_data["isbn"]
        )
        db.session.add(book)
        db.session.commit()
        return 'OK', 200

    message = {'Endpoint' : 'Add Book',
                'Description' : 'Used to register book in db'}
    return jsonify(message)

@listing_blueprint.route('/api/listing', methods=['GET','POST'])
def addListing():
    if request.method == "POST":

        photo = request.files["photo"]
        photo = photo.read()
        listing_data = request.get_json()

        listing = Listing(
            photo,
            listing_data["description"],
            int(listing_data["condition"]),
            int(listing_data["no_available"]),
            float(listing_data["price"]),
            int(listing_data["user_id"]),
            int(listing_data["book_id"])
        )
        db.session.add(listing)
        db.session.commit()
        return 'OK', 200

    message = {'Endpoint' : 'Add Listing',
                'Description' : 'Used to register listing in db'}
    return jsonify(message)

@request_blueprint.route('/api/request', methods=['GET','POST'])
def addRequest():
    if request.method == "POST":
        request_data = request.get_json()

        request = Request(
            int(request_data["condition"]),
            float(request_data["money"]),
            int(request_data["user_id"]),
            int(request_data["book_id"])
        )
        db.session.add(request)
        db.session.commit()
        return 'OK', 200

    message = {'Endpoint' : 'Add Request',
                'Description' : 'Used to register request in db'}
    return jsonify(message)