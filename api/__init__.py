from flask import Flask
from api.extensions import db
from api.auth import auth_blp
from api.config import config_dict


def create_app(config_name='development'):

    # set the configuration
    config_class = config_dict[config_name]

    app = Flask(__name__)
    db.init_app(app)

    app.register_blueprint(auth_blp)
    return app
