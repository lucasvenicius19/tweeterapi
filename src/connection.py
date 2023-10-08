from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://lucas:usxJH7YdDLn1dUzA@cluster0.7riiya3.mongodb.net/")

db = client.dio_live

trends_collection = db.trends