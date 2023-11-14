from flask import Flask
from api.extensions import db
from api.auth import auth_blp


def create_app():
    app = Flask(__name__)
    db.init_app(app)

    app.register_blueprint(auth_blp)
    return app
