from flask import request, jsonify, Blueprint
from .models.user import User
from .models.book import Book
from .models.request import Request
from .models.listing import Listing
from .models.chat import Chat
from .models.userchat import UserChat
from .models.message import Message
from app import db

user_blueprint = Blueprint("user_blueprint", __name__)
book_blueprint = Blueprint("book_blueprint", __name__)
listing_blueprint = Blueprint("listing_blueprint", __name__)
request_blueprint = Blueprint("request_blueprint", __name__)
#chat_blueprint = Blueprint("chat_blueprint", __name__) //Not needed for now

@user_blueprint.route('/')
def index():
    return "<h1>Back end</h1>"

@user_blueprint.route('/api/user', methods=['GET', 'POST', 'DELETE'])
def userMethods():
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
    
    if request.method == "DELETE":
        user_data = request.get_json()

        uid = user_data['id']

        delUser = User.query.filter_by(id = uid).first()

        if delUser:
            db.session.delete(delUser)
            db.session.commit()
            return 'OK', 200

    message = {'Endpoint' : 'User',
                'Description' : 'Used to register/edit/delete user in db'}
    return jsonify(message)

@book_blueprint.route('/api/book', methods=['GET','POST'])
def bookMethods():
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

    if request.method == "DELETE":
        book_data = request.get_json()

        bid = book_data['id']

        delBook = Book.query.filter_by(id = bid).first()

        if delBook:
            db.session.delete(delBook)
            db.session.commit()
            return 'OK', 200
        
        return 'Internal Server Error', 500

    message = {'Endpoint' : 'Book',
                'Description' : 'Used to register/edit/delete book in db'}
    return jsonify(message)

@listing_blueprint.route('/api/listing', methods=['GET','POST'])
def listingMethods():
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

    if request.method == "DELETE":
        listing_data = request.get_json()

        lid = listing_data['id']

        delListing = Listing.query.filter_by(id = lid).first()

        if delListing:
            db.session.delete(delListing)
            db.session.commit()
            return 'OK', 200
        
        return 'Internal Server Error', 500

    message = {'Endpoint' : 'Add Listing',
                'Description' : 'Used to register/edit/delete listing in db'}
    return jsonify(message)

@request_blueprint.route('/api/request', methods=['GET','POST'])
def requestMethods():
    if request.method == "POST":
        request_data = request.get_json()

        req = Request(
            int(request_data["condition"]),
            float(request_data["money"]),
            int(request_data["user_id"]),
            int(request_data["book_id"])
        )
        db.session.add(req)
        db.session.commit()
        return 'OK', 200

    if request.method == "DELETE":
        req_data = request.get_json()

        rid = req_data['id']

        delRequest = User.query.filter_by(id = rid).first()

        if delRequest:
            db.session.delete(delRequest)
            db.session.commit()
            return 'OK', 200
        
        return 'Internal Server Error', 500

    message = {'Endpoint' : 'Add Request',
                'Description' : 'Used to register/edit/delete request in db'}
    return jsonify(message)

##@chat_blueprint.route('api/chat', methods=['GET', 'POST'])
##def createChat():
    ##if request.method == "POST":
        ##chat_data = request.get_json()

        ##chat = Chat()
        ##chat_id = chat.id

        ##pass      // Nothing here is needed for now