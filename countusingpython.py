from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime

uri = "mongodb+srv://keerthi2556:Reddy2002@cluster0.3wm2fac.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    # Get reference to 'sample_training' database
    db = client.sample_training

    # Get reference to 'zips' collection
    accounts_collection = db.zips

    new = [{"$count":"total_zips"}]

    result = list(accounts_collection.aggregate(new))

    if result:
        print(result)
    else:
        print("No documents in the collection")


except Exception as e:
    print(e)
finally:
    client.close()
