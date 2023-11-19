from flask import Blueprint, request, jsonify
from api.models import Books, BookGenre, Users
from api.decorator import admin_required
from flask_jwt_extended import jwt_required, get_jwt_identity

users_blp = Blueprint('users', __name__)


@users_blp.route('/users', methods=['GET'])
@jwt_required()
@admin_required
def get_users():
    try:
        users = Users.query.all()
        users_list = []
        for user in users:
            users_list.append({
                "id": user.id,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "username": user.username,
                "email": user.email,
                "is_admin": user.is_admin
            })
        return jsonify({"users": users_list}), 200
    except Exception as e:
        print(e, "error")
        return jsonify({"message": "An error occurred"}), 400


# user dashboard
@users_blp.route('/dashboard', methods=['GET'])
@jwt_required()
def dashboard():
    try:
        username = get_jwt_identity()
        user = Users.query.filter_by(username=username).first()
        if not user:
            return jsonify({"message": "User does not exist"}), 400
        return jsonify({
            "id": user.id,
            "firstname": user.firstname,
            "lastname": user.lastname,
            "username": user.username,
            "email": user.email,
            "is_admin": user.is_admin
        }), 200
    except Exception as e:
        print(e, "error")
        return jsonify({"message": "An error occurred"}), 400
