from os import environ
from pymongo import MongoClient

client = MongoClient(environ.get("MONGO_URL"))

db = client.db_chat
