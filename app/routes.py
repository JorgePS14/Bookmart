from flask import request, jsonify, Blueprint
from .models.user import User
from .models.book import Book
from .models.request import Request
from .models.listing import Listing
from flask_cors import CORS, cross_origin
import time
import boto3
# from flask_jwt import jwt_required, current_identity
from app import db
from os import environ

user_blueprint = Blueprint("user_blueprint", __name__)
book_blueprint = Blueprint("book_blueprint", __name__)
listing_blueprint = Blueprint("listing_blueprint", __name__)
request_blueprint = Blueprint("request_blueprint", __name__)


@user_blueprint.route('/api/user', methods=['GET', 'POST', 'DELETE'])
@user_blueprint.route('/api/user/<int:id>', methods=['DELETE'])
@user_blueprint.route('/api/user/<email>', methods=['GET'])
@user_blueprint.route('/api/user/<int:id>', methods=['GET'])
def userMethods(id=None, email=None):
    if request.method == "GET":
        if email != None:
            user = User.query.filter_by(email=email).first()
            print(user.email)
            if user:
                return {
                    "email": user.email,
                    "username": user.username,
                    "location": user.location,
                    "university": user.university,
                    "semester": user.semester,
                    "major": user.major
                }
            else:
                return {}
        elif id != None:
            user = User.query.filter_by(id=id).first()
            if user:
                return {
                    "email": user.email,
                    "username": user.username,
                    "location": user.location,
                    "university": user.university,
                    "semester": user.semester,
                    "major": user.major
                }

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


@book_blueprint.route('/api/book', methods=['POST'])
@book_blueprint.route('/api/book/<int:id>', methods=['GET'])
@book_blueprint.route('/api/book/<int:id>', methods=['DELETE'])
def bookMethods(id=None):
    if request.method == "GET":
        book = Book.query.filter_by(id=id).first()
        return {
            "name": book.name,
            "author": book.author,
            "edition": book.edition,
            "value": book.value,
            "isbn": book.isbn
        }

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
@listing_blueprint.route('/api/listing/<int:idNo>', methods=['DELETE'])
def listingMethods(idNo=None):
    if request.method == "POST":
        listing_data_description = request.form.get('description')
        listing_data_condition = int(request.form.get('condition'))
        listing_data_no_available = int(request.form.get('no_available'))
        listing_data_price = float(request.form.get('price'))
        listing_data_user_id = int(request.form.get('user_id'))
        listing_data_book_id = int(request.form.get('book_id'))

        photo = request.files["photo"]
        photo_name = None
        if photo:
            name = photo.filename
            timestr = time.strftime("%Y%m%d-%H%M%S")
            name = timestr+name
            s3_client = boto3.client('s3')
            response = s3_client.upload_fileobj(photo, environ.get("AWS_BUCKET"), name, ExtraArgs={'ACL': 'public-read', 'ContentType': 'image/jpeg'})
            photo_name = environ.get("AWS_S3_PATH")+name

        listing = Listing(
            photo_name,
            listing_data_description,
            listing_data_condition,
            listing_data_no_available,
            listing_data_price,
            listing_data_user_id,
            listing_data_book_id
        )
        db.session.add(listing)
        db.session.commit()
        return 'OK', 200

    elif request.method == "DELETE":

        delListing = Listing.query.filter_by(id=idNo).first()

        if delListing:
            db.session.delete(delListing)
            db.session.commit()
            return 'OK', 200

        print("Found nothing")
        
        return 'Internal Server Error', 500

    if idNo:
        listing = Listing.query.filter_by(id = id).first()
        if listing:
            return jsonify({'photo': listing.photo, 'description': listing.description, 
                            'condition': listing.condition, 'no_available': listing.no_available,
                            'price': listing.price, 'user_id': listing.user_id, 'book_id': listing.book_id})
        return jsonify({'Endpoint' : 'Listing',
                'Message' : 'The listing was not found'}), 404

    if request.get_json():
        request_data = request.get_json()
        name = request_data["name"]

        books = Book.query.filter(Book.name.contains(name)).all()

        bookIds = []

        for book in books:
            bookIds.append(book.id)

        response = []

        for bookId in bookIds:
            listings = Listing.query.filter_by(book_id = bookId).all()
            if listings:
                for listing in listings:
                    response.append({'id': listing.id, 'photo': str(listing.photo), 'description': listing.description, 
                                'condition': listing.condition, 'no_available': listing.no_available,
                                'price': listing.price, 'user_id': listing.user_id, 'book_id': listing.book_id})
        
        return jsonify(response), 200

    listings = Listing.query.order_by(Listing.id).all()
    print(listings)
    response = []
    for listing in listings:
        response.append({'id': listing.id, 'photo': str(listing.photo), 'description': listing.description, 
                            'condition': listing.condition, 'no_available': listing.no_available,
                            'price': listing.price, 'user_id': listing.user_id, 'book_id': listing.book_id})
    return jsonify(response), 200

@request_blueprint.route('/api/request', methods=['GET','POST'])
@request_blueprint.route('/api/request/<int:idNo>', methods=['DELETE', 'GET'])
def requestMethods(idNo=None):
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

        delRequest = Request.query.filter_by(id=idNo).first()

        if delRequest:
            db.session.delete(delRequest)
            db.session.commit()
            return 'OK', 200
        
        print("Found nothing")
        
        return 'Could not delete the book because it was not found', 404

    if idNo:
        req = Request.query.filter_by(id = id).first()
        if req:
            return jsonify({'condition': req.condition, 'money': req.money, 
                            'user_id': req.user_id, 'book_id': req.book_id})
        return jsonify({'Endpoint' : 'Request',
                'Message' : 'The request was not found'}), 404

    reqs = Request.query.order_by(Request.id).all()
    print(reqs)
    response = []
    for req in reqs:
        response.append({'id':req.id, 'condition':req.condition, 'money':req.money,
                        'user_id':req.user_id, 'book_id':req.book_id})
    return jsonify(response), 200