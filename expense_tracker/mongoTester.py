from pymongo import MongoClient
import datetime
import pprint


client = MongoClient('mongodb://127.0.0.1:27017/')
db = client.mydb
collection = db.mycollection

post = {"author": "Mike",
		"text": "My first blog post!",
		"tags": ["mongodb", "python", "pymongo"],
		"date": datetime.datetime.utcnow()}
		
post_id = collection.insert_one(post).inserted_id
print(post_id)
pprint.pprint(collection.find_one())
