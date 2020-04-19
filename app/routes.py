from flask import request, jsonify, Blueprint
from .models.user import User
from .models.book import Book
from .models.request import Request
from .models.listing import Listing
import json
# from flask_jwt import jwt_required, current_identity
from app import db

user_blueprint = Blueprint("user_blueprint", __name__)
book_blueprint = Blueprint("book_blueprint", __name__)
listing_blueprint = Blueprint("listing_blueprint", __name__)
request_blueprint = Blueprint("request_blueprint", __name__)
#chat_blueprint = Blueprint("chat_blueprint", __name__) //Not needed for now


@user_blueprint.route('/api/user', methods=['GET', 'POST', 'DELETE'])
@user_blueprint.route('/api/user/<int:id>', methods=['DELETE'])
def userMethods(id=None):
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

        delUser = User.query.filter_by(id=id).first()

        if delUser:
            db.session.delete(delUser)
            db.session.commit()
            return 'OK', 200

        print("Found nothing")

    message = {'Endpoint' : 'User',
                'Description' : 'Used to register/edit/delete user in db'}
    return jsonify(message)

@book_blueprint.route('/api/book', methods=['GET','POST'])
@ book_blueprint.route('/api/book/<int:id>', methods=['DELETE'])
def bookMethods(id=None):
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

    elif request.method == "DELETE":

        delBook = Book.query.filter_by(id=id).first()

        if delBook:
            db.session.delete(delBook)
            db.session.commit()
            return 'OK', 200

        print("Found nothing")
        
        return 'Internal Server Error', 500

    message = {'Endpoint' : 'Book',
                'Description' : 'Used to register/edit/delete book in db'}
    return jsonify(message)

@listing_blueprint.route('/api/listing', methods=['GET','POST'])
@listing_blueprint.route('/api/listing/<int:id>', methods=['DELETE'])
def listingMethods(id=None):
    if request.method == "POST":
        listing_data = request.get_json()

        #if request.files["photo"]:
        #    photo = request.files["photo"]
        #    photo = photo.read()

        listing = Listing(
            #photo,
            listing_data["photo"],
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

    elif request.method == "DELETE":

        delListing = Listing.query.filter_by(id=id).first()

        if delListing:
            db.session.delete(delListing)
            db.session.commit()
            return 'OK', 200

        print("Found nothing")
        
        return 'Internal Server Error', 500

    message = {'Endpoint' : 'Add Listing',
                'Description' : 'Used to register/edit/delete listing in db'}
    return jsonify(message)

@request_blueprint.route('/api/request', methods=['GET','POST'])
@request_blueprint.route('/api/request/<int:id>', methods=['DELETE'])
def requestMethods(id=None):
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

        delRequest = Request.query.filter_by(id=id).first()

        if delRequest:
            db.session.delete(delRequest)
            db.session.commit()
            return 'OK', 200
        
        print("Found nothing")
        
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
