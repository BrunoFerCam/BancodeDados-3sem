import json
import redis
from pymongo.mongo_client import MongoClient
uri = "mongodb+srv://brunofernandescampos:<password>@cluster0.09dtabz.mongodb.net/?appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri)
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
    
conR = redis.Redis(host='redis-16476.c44.us-east-1-2.ec2.redns.redis-cloud.com',
                  port=16476,
                  password='sMgmFFmxPDpa789K2rEClugvRp58dulj')

#conR.set("user-diogo","Diogo")

print(conR.get("user-diogo"))
               
