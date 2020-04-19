from datetime import timedelta
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from .routes import user_blueprint, book_blueprint, listing_blueprint, request_blueprint


def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_DATABASE_URI'] = '%s://%s:%s@%s/%s' % (
        app.config.get("DB_CONNECTION"),
        app.config.get("DB_USERNAME"),
        app.config.get("DB_PASSWORD"),
        app.config.get("DB_HOST"),
        app.config.get("DB_NAME"),
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.config['JWT_EXPIRATION_DELTA'] = timedelta(seconds=86400)
    app.config['JWT_AUTH_USERNAME_KEY'] = 'email'

    # Initialize plugins
    db.init_app(app)

    with app.app_context():
        from app.models import user, book, listing
        from . import auth

        db.create_all()
        db.session.commit()

        app.register_blueprint(user_blueprint)
        app.register_blueprint(auth.auth_bp)
        app.register_blueprint(book_blueprint)
        app.register_blueprint(listing_blueprint)
        app.register_blueprint(request_blueprint)
        #app.register_blueprint(chat_blueprint) //Not needed for now
        
        return app
