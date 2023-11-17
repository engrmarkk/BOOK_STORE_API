from flask import Flask
from api.extensions import db, migrate
from api.auth import auth_blp
from api.config import config_dict
from api.models import *


def create_app(configure=config_dict["development"]):
    app = Flask(__name__)
    app.config.from_object(configure)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(auth_blp)
    return app
