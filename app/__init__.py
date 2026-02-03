from flask import Flask 
from .config import Config
from .blueprints import register_all_blueprint
from .core.db import db_close


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_all_blueprint(app)
    app.teardown_request(db_close)


    return app