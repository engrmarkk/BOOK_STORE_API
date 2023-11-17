from flask import Blueprint, request, jsonify
from api.util import check_if_email_exists, check_if_username_exists
from api.models import Users
from passlib.hash import pbkdf2_sha256 as sha256
from flask_jwt_extended import create_access_token, create_refresh_token

auth_blp = Blueprint('auth', __name__)


@auth_blp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        print(data, type(data), "data")

        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({"message": "All fields are required"}), 400

        if not check_if_email_exists(email.lower()):
            return jsonify({"message": "Email does not exist"}), 400

        user = Users.query.filter_by(email=email.lower()).first()
        if not sha256.verify(password, user.password):
            return jsonify({"message": "Incorrect password"}), 400

        access_token = create_access_token(identity=user.username)
        refresh_token = create_refresh_token(identity=user.username)

        return jsonify({
            "message": "login successful",
            "access_token": access_token,
            "refresh_token": refresh_token
        }), 200
    except KeyError:
        return jsonify({"message": "All fields are required"}), 400
    except Exception as e:
        print(e, "error")
        return jsonify({"message": "An error occurred"}), 400


@auth_blp.route('/register', methods=['POST'])
def register():
    try:
        data = request.json

        firstname = data.get('firstname')
        lastname = data.get('lastname')
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not firstname or not lastname or not username or not email or not password:
            return jsonify({"message": "All fields are required"}), 400
        if (
                not "firstname" in data or not "lastname" in data or not "username" in data or not "email" in data or not "password" in data):
            return jsonify({"message": "All fields are required"}), 400

        if check_if_email_exists(email.lower()):
            return jsonify({"message": "Email already exists"}), 400

        if check_if_username_exists(username.lower()):
            return jsonify({"message": "Username already exists"}), 400

        hashed_password = sha256.hash(password)

        user = Users(
            firstname=firstname.lower(),
            lastname=lastname.lower(),
            username=username.lower(),
            email=email.lower(),
            password=hashed_password
        )
        user.save()

    except KeyError:
        return jsonify({"message": "All fields are required"}), 400
    except Exception as e:
        print(e, "error")
        return jsonify({"message": "An error occurred"}), 400
