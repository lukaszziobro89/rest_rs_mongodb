#!/bin/env python
from flask import Flask
from domain.user import user_blueprint
from domain.hello_world import hello_world_blueprint


def create_flask_app():
    flask_app = Flask(__name__)
    flask_app.register_blueprint(user_blueprint)
    flask_app.register_blueprint(hello_world_blueprint)
    return flask_app


if __name__ == '__main__':
    app = create_flask_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.app_context().push()
