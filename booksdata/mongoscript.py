from pymongo import MongoClient
import datetime
from dotenv import load_dotenv
import os

user = os.getenv('username')
password = os.getenv("password")
client = MongoClient('mongodb+srv://{user}:{password}@cluster0.bfjclhv.mongodb.net/')

db = client.scrapy

posts = db.test_collection

doc = post = {
    "author": "Mike",
    "text": "My first blog post!",
    "tags": ["mongodb", "python", "pymongo"],
    "date": datetime.datetime.now(tz=datetime.timezone.utc)}

post_id = posts.insert_one(post).inserted_id
