from flask import Flask
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

    @app.route('/')
    def index():
        return "<h1>Back end</h1>"

    return app


app = create_app()
db = SQLAlchemy(app)

from app.models import user, book, listing

db.create_all()
db.session.commit()
