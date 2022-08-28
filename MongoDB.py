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
        print(record)
        return True if record else False

    def search(self, collection, text, field_to_search_by):
        col = self.get_collection(collection)
        cursor = col.find({field_to_search_by: {'$regex': text}})
        return [record for record in cursor] if cursor else []
