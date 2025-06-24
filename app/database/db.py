from pymongo import MongoClient

client = MongoClient("mongodb://root:root@localhost:27017")
db = client.project_manager