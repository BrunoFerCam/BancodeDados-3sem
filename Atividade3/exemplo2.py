
import json
import redis
from pymongo.mongo_client import MongoClient

uri = "mongodb+srv://brunofernandescampos:FJwbzZ2dq5I22HIH@cluster0.09dtabz.mongodb.net/?appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, ssl_cert_reqs=ssl.CERT_NONE)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)