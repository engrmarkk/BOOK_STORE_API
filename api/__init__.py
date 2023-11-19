from flask import Flask
from api.extensions import db, migrate, jwt_manager
from api.auth import auth_blp
from api.endpoints import books_blp, users_blp
from api.config import config_dict
from api.models import *


def create_app(configure=config_dict["development"]):
    app = Flask(__name__)
    app.config.from_object(configure)

    db.init_app(app)
    migrate.init_app(app, db, render_as_batch=True)
    jwt_manager.init_app(app)

    app.register_blueprint(auth_blp)
    app.register_blueprint(books_blp)
    app.register_blueprint(users_blp)
    return app
