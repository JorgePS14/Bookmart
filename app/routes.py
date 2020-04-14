from flask import request, jsonify, Blueprint
from .models.user import User
from .models.listing import Listing
from app import db


user_blueprint = Blueprint("user_blueprint", __name__)


@user_blueprint.route('/')
def index():
    return "<h1>Back end</h1>"


@user_blueprint.route("/api/user", methods=["POST", "GET"])
def updateUser():
    # POST request
    if request.method == 'POST':
        user_data = request.get_json()
        print(request.get_json())
        new_user = User(
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
    elif request.method == 'GET':
        message = {'greeting': 'Hello from flask'}
        return jsonify(message)
