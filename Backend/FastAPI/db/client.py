from pymongo import MongoClient

# db_client = MongoClient().local

db_client = MongoClient("mongodb+srv://test:test@cluster0.ytwpy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0").test