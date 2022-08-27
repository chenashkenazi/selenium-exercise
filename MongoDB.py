import pymongo


class MongoDB:

    def __init__(self, connection_string):
        self.client = pymongo.MongoClient(connection_string)

    def get_collection(self, collection):
        db = self.client["exercise"]
        return db[collection]

    def insert(self, collection, record):
        col = self.get_collection(collection)
        col.insert_one(record)

    def check_existence(self, collection, field, value):
        col = self.get_collection(collection)
        record = col.find_one({field: value})
        return True if record else False

    def search(self, collection, text):
        col = self.get_collection(collection)
        print("I will search!")