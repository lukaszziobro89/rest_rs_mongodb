from flask import Blueprint
from flask import jsonify
from app.config.mongo import create_mongo_client
import os

ENDPOINT_MESSAGE = os.environ.get('ENDPOINT_MESSAGE')

MONGO_CLIENT = create_mongo_client()

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/')
def hello_world():
    message = '{0} {1}'.format("MESSAGE:", ENDPOINT_MESSAGE)
    return jsonify({"message": message})


@user_blueprint.route('/user')
def user():
    return jsonify({"message": "package_test"})


@user_blueprint.route("/<db>/<collection>", methods=['GET'])
def get_all_users(db, collection):
    pymongo_cursor = MONGO_CLIENT[db][collection].find()
    data = []
    for doc in pymongo_cursor:
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    return jsonify(data)


@user_blueprint.route("/<db>/<collection>/<int:id>", methods=['GET'])
def get_user_by_id(db, collection, id):
    pymongo_cursor = MONGO_CLIENT[db][collection].find({"id": id})
    data = []
    for doc in pymongo_cursor:
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    return jsonify(data)


@user_blueprint.route('/package2')
def package_test2():
    return jsonify({"message": "package_test"})
