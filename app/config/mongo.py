import pymongo


def create_mongo_client():
    mongo_client = pymongo.MongoClient("mongodb://mongo_1:27017")
    return mongo_client
