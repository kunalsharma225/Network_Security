
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://bhediyasharma377:Admin123@cluster0.g97nc8j.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(uri)

try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)