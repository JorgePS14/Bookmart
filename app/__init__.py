from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

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


    CORS(app)
    @app.route("/api/user", methods=["POST", "GET"])
    def updateUser():
        # POST request
        if request.method == 'POST':
            user_data = request.get_json()
            
            new_user = user.User(
                user_data["email"],
                user_data["password"],
                user_data["username"],
                user_data["location"],
                user_data["university"],
                user_data["semester"],
                user_data["major"]
            )

            db.session.add(new_user)
            db.session.commit()
                
            return 'OK', 200
        
        # GET request
        else:
            message = {'greeting':'Hello from flask'}
            return jsonify(message)

    return app


app = create_app()
db = SQLAlchemy(app)

from app.models import user

db.create_all()
db.session.commit()

if __name__ == "__main__":
    app.run()