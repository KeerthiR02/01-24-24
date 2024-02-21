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
    new_account = {

"Month": "January",
"Category": "Food",
"Description": "outside Food",
"Date": "21-01-24",
"Type": "Card",
"Amount":50.0

}

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = accounts_collection.insert_one(new_account)

    document_id = result.inserted_id
    pprint(f"_id of inserted document: {document_id}")


except Exception as e:
    print(e)
finally:
    client.close()