import os
import pwd

from flask import Blueprint, jsonify

hello_world_blueprint = Blueprint('hello_world_blueprint', __name__)

ENDPOINT_MESSAGE = os.environ.get('ENDPOINT_MESSAGE')


@hello_world_blueprint.route('/')
def hello_world():
    message = '{0} {1}'.format("MESSAGE:", ENDPOINT_MESSAGE)
    return jsonify({"message": message})


@hello_world_blueprint.route('/user')
def user():
    username = pwd.getpwuid(os.getuid())[0]
    return jsonify({"message": username})
