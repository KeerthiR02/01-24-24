from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
from pprint import pprint
uri = "mongodb+srv://keerthi2556:Reddy2002@cluster0.eaiaoy5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))


try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    
    db = client.Monthly_Expense

    # Get reference to 'accounts' collection
    accounts_collection = db.Transactions

    # inserting one account
    doccument_to_find = {
        '1': ObjectId('65d632f2834a2f0dd77e0a79'),
    }

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = accounts_collection.insert_one(doccument_to_find)

    pprint.pprint(result)


except Exception as e:
    print(e)
finally:
    client.close()