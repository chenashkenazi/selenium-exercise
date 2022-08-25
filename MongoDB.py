import pymongo


class MongoDB:

    def __init__(self):
        client = pymongo.MongoClient(host="0.0.0.0", port=2717)

    def get_collection(self, collection):
        db = client["exercise"]
        return client[collection]

    def insert(self, collection, record):
        col = self.get_collection(collection)
        col.insert_one(record)

    def search(self, collection, text):
        col = self.get_collection(collection)
        print("I will search!")