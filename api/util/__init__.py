from api.models import *


def check_if_email_exists(email):
    user = Users.query.filter_by(email=email).first()
    if user:
        return True
    return False


def check_if_username_exists(username):
    user = Users.query.filter_by(username=username).first()
    if user:
        return True
    return False
