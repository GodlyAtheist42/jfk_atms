from flask import Flask
from .extensions import mongo, bcrypt
from .main import main


def create_app(config_object='source.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    mongo.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(main)

    return app