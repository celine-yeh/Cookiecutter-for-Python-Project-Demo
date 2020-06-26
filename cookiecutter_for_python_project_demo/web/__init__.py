from flask import Flask, jsonify

from .views import blueprint as web
from .. import __version__, config


def create_app():
    app = Flask(__name__)
    app.debug = config.debug

    @app.route('/health')
    def health():  # pylint: disable=unused-variable
        return jsonify(version=__version__)

    app.register_blueprint(web)
    return app

application = create_app()
