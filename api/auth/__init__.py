from flask import Blueprint

auth_blp = Blueprint('auth', __name__)


@auth_blp.route('/test')
def test():
    return 'auth test'
