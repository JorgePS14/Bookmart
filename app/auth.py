from flask import Blueprint, request
from .models.user import User
from app import db
from flask import current_app as app
from flask_jwt import JWT


# Blueprint configuration
auth_bp = Blueprint('auth_bp', __name__)


@auth_bp.route('/signup', methods=['POST'])
def signup():
    """POST: If form is valid, creates a user."""
    data = request.get_json()
    response = {}

    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    if not password:
        response["message"] = "No password was given"
        response["status"] = 400
        return response

    location = data.get('location')
    university = data.get('university')
    semester = int(data.get('semester'))
    major = data.get('major')

    user = User(
        email,
        username,
        location,
        university,
        semester,
        major
    )
    user.set_password(password)

    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        response["db"] = {
            "message": e.args[0]
        }
        response["status"] = 400
        return response

    response["message"] = "Ok"
    response["status"] = 200
    return response


def authenticate(email, password):
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password=password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)


jwt = JWT(app, authenticate, identity)
