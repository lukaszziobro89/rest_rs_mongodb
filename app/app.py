#!/bin/env python
import os
import pymongo
import json
from flask import Flask, request, jsonify


app = Flask(__name__)
app.app_context().push()

myclient = pymongo.MongoClient("mongodb://mongo_1:27017")

ENDPOINT_MESSAGE = os.environ.get('ENDPOINT_MESSAGE')


@app.route('/')
def hello_world():
    return '{0} {1}'.format("MESSAGE:", ENDPOINT_MESSAGE)


@app.route('/user')
def user():
   return 'user'


@app.route("/<db>/<collection>", methods=['GET'])
def get_all_users(db, collection):
    pymongo_cursor = myclient[db][collection].find()
    data = []
    for doc in pymongo_cursor:
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    return jsonify(data)


@app.route("/<db>/<collection>/<id>", methods=['GET'])
def get_user_by_id(db, collection, id):
    pymongo_cursor = myclient[db][collection].find({"id":id})
    data = []
    for doc in pymongo_cursor:
        doc['_id'] = str(doc['_id'])
        data.append(doc)
    return jsonify(data)
