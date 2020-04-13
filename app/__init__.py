from flask import Flask, url_for, request, redirect, send_file, Blueprint, flash, send_from_directory, after_this_request
from flask_sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)

    app.config.from_pyfile('settings.py')

    app.config['SQLALCHEMY_DATABASE_URI'] = '%s://%s:%s@%s/%s' % (
        app.config.get("DB_CONNECTION"),
        app.config.get("DB_USERNAME"),
        app.config.get("DB_PASSWORD"),
        app.config.get("DB_HOST"),
        app.config.get("DB_NAME"),
    )

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    return app

app = create_app()
db = SQLAlchemy(app)

from app.models import user, book, listing

db.create_all()
db.session.commit()

@app.route('/')
def index():
    return "<h1>Back end</h1>"

@app.route('/addBook', methods=['GET','POST'])
def addBook():
    if request.method == "POST":
        name = request.form["name"]
        author = request.form["author"]
        edition = request.form["edition"]
        value = request.form["value"]
        isbn = request.form["isbn"]
        from app.models import book
        book = book.Book(name = name, author = author, edition = edition, value = value, isbn = isbn)
        db.session.add(book)
        db.session.commit()
        return '<h1>Book added</h1>'
    return '<h1>Add book endpoint -- Try using Postman</h1>'

@app.route('/addListing', methods=['GET','POST'])
def addListing():
    if request.method == "POST":
        photo = request.files["photo"]
        photo = photo.read()
        description = request.form["description"]
        condition = int(request.form["condition"])
        no_available = int(request.form["no_available"])
        price = float(request.form["price"])
        user_id = request.form["user_id"]
        book_id = request.form["book_id"]
        from app.models import listing
        listing = listing.Listing(photo = photo, description = description, condition = condition, no_available = no_available, price = price, user_id = user_id, book_id = book_id)
        db.session.add(listing)
        db.session.commit()
        return '<h1>Listing added</h1>'
    return '<h1>Add listing endpoint -- Try using Postman</h1>'