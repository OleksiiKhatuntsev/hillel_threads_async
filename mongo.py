from pymongo import MongoClient
import json

mongo_client = MongoClient("mongodb://localhost:27017/")

db = mongo_client["test_hillel_db"]

collection = db["characters_collection_1"]
# SELECT email from collection WHERE email = iknownothing@gmail.com
for x in collection.find({"email": "iknownothing@gmail.com"},{}):
    print(x)

# collection.insert_one({"tea_name": "lipton"})
tea = collection.find_one({"tea_name": "lipton"}, {})
print(type(tea))
# collection.update_many()
collection.update_one({"tea_name": "lipton"}, {"$set": {"tea_name": "greenfield"}})
# print(collection.find().limit(10))