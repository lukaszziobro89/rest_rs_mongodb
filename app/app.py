#!/bin/env python
from flask import Flask
from domain.user import user_blueprint


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)
    app.app_context().push()
