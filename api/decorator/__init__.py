from functools import wraps
from flask import request, jsonify
from flask_jwt_extended import get_jwt_identity
from api.util import check_if_admin


def admin_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            current_user = get_jwt_identity()
            print(current_user, "current_user")
            if not current_user:
                return jsonify({"message": "Unauthorized"}), 401
            if not check_if_admin(current_user):
                return jsonify({"message": "Unauthorized, You are not an admin"}), 401
            return func(*args, **kwargs)
        except Exception as e:
            print(e, "error")
            return jsonify({"message": "An error occurred"}), 400

    return wrapper
