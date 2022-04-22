from flask import Flask
from app.routes import init_routes
import config


def create_app() -> Flask:
    app = Flask(__name__,
                static_folder=config.STATIC_FOLDER,
                template_folder=config.TEMPLATE_FOLDER)
    app.config.from_object(config)
    init_routes(app)

    return app
