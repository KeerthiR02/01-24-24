
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


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import datetime
uri = "mongodb+srv://keerthi2556:Reddy2002@cluster0.eaiaoy5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))





try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    
    db = client.Monthly_Expense

    accounts_collection = db.Transactions


    # inserting many accounts
    new_accounts = [
  {
"Month": "January",
"Category": "Food",
"Description": "outside Food",
"Date": "21-01-24",
"Type": "Card",
"Amount":"50.0"

},

{ 

"Month": "February",
"Category": "Groceries",
"Description": "vegetables",
"Date": "25-02-24",
"Type": "Cash",
"Amount":"140.0"

},

{ 

"Month": "March",
"Category": "rent",
"Description": "House Rent",
"Date": "01-03-24",
"Type": "Cash",
"Amount":"600.0"


},

{

"Month": "April",
"Category": "Electricity bill",
"Description": "Utilities",
"Date": "01-04-24",
"Type": "Card",
"Amount":"140.0"

},
{

"Month": "May",
"Category": "movie",
"Description": "movie ticket",
"Date": "06-05-24",
"Type": "Card",
"Amount":"200.0"

},
{

"Month": "June",
"Category": "Birthday",
"Description": "Birthday Party",
"Date": "06-06-24",
"Type": "Card",
"Amount":"1500.0"

}
]

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = accounts_collection.insert_many(new_accounts)

    document_ids = result.inserted_ids
    print("# of documents inserted: " + str(len(document_ids)))
    print(f"_ids of inserted documents: {document_ids}")


except Exception as e:
    print(e)
finally:
    client.close()

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
        '_id': ObjectId('65d658b33c67f6e861331c2b'),
    }

    # Write an expression that inserts the 'new_account' document into the 'accounts' collection.
    result = accounts_collection.Find_one(doccument_to_find)

    pprint.pprint(result)


except Exception as e:
    print(e)
finally:
    client.close()

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
    documents_to_find = {"Type":"Cash"}

    # Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
    cursor = accounts_collection.find(documents_to_find)

    num_docs = 0
    for document in cursor:
        num_docs += 1
        pprint.pprint(document)
        print()
    print("# of documents found: " + str(num_docs))


except Exception as e:
    print(e)
finally:
    client.close()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint
uri = "mongodb+srv://keerthi2556:Reddy2002@cluster0.eaiaoy5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

   
    db = client.Monthly_Expense

    # Get reference to 'accounts' collection
    accounts_collection = db.Transactions

    # Filter
    document_to_update = {'_id': ObjectId('65d658d5e41f462db6f8fb36')}

    # Update
    add_to_balance = {"$inc": {"Amount": 150}}

    # Print original document
    pprint.pprint(accounts_collection.find_one(document_to_update))

    # Write an expression that adds to the target account balance by the specified amount.
    result = accounts_collection.update_one(document_to_update, add_to_balance)
    print("Documents updated: " + str(result.modified_count))

    # Print updated document
    pprint.pprint(accounts_collection.find_one(document_to_update))


except Exception as e:
    print(e)
finally:
    client.close()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint
uri = "mongodb+srv://keerthi2556:Reddy2002@cluster0.eaiaoy5.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

   
    db = client.Monthly_Expense

    # Get reference to 'accounts' collection
    accounts_collection = db.Transactions

    # Filter
    select_accounts = {"type": "card"}

    # Print original document
    set_field = {"$set": {"Amount": 50.0}}

    # Write an expression that adds to the target account balance by the specified amount.
    result = accounts_collection.update_many(select_accounts, set_field)

    # Print updated document
    print("Documents matched: " + str(result.matched_count))
    print("Documents updated: " + str(result.modified_count))
    pprint.pprint(accounts_collection.find_one(select_accounts))

except Exception as e:
    print(e)
finally:
    client.close()

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://keerthi2556:Reddy2002@cluster0.eaiaoy5.mongodb.net/?retryWrites=true&w=majority"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

   
    db = client.Monthly_Expense

    # Get reference to 'accounts' collection
    accounts_collection = db.Transactions

    # Filter by ObjectId
    document_to_delete = {"_id": ObjectId("65d65c1296f22ef88d76f1c9")}

    # Search for document before delete
    print("Searching for target document before delete: ")
    pprint.pprint(accounts_collection.find_one(document_to_delete))

    # Write an expression that deletes the target account.
    result = accounts_collection.delete_one(document_to_delete)

    # Search for document after delete
    print("Searching for target document after delete: ")
    pprint.pprint(accounts_collection.find_one(document_to_delete))

    print("Documents deleted: " + str(result.deleted_count))


except Exception as e:
    print(e)
finally:
    client.close()
#deleteManyUsingCRUD
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId
import pprint

uri = "mongodb+srv://keerthi2556:Reddy2002@cluster0.eaiaoy5.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

try:
    # Send a ping to confirm a successful connection
    client.admin.command('ping')

    
    db = client.Monthly_Expense

    # Get reference to 'accounts' collection
    accounts_collection = db.Transactions

    # Filter by ObjectId
    documents_to_delete = {"Amount": {"$lt": 100.0}}

    # Search for sample document before delete
    print("Searching for sample target document before delete: ")
    pprint.pprint(accounts_collection.find_one(documents_to_delete))

    # Write an expression that deletes the target accounts.
    result = accounts_collection.delete_many(documents_to_delete)

    # Search for sample document after delete
    print("Searching for sample target document after delete: ")
    pprint.pprint(accounts_collection.find_one(documents_to_delete))

    print("Documents deleted: " + str(result.deleted_count))


except Exception as e:
    print(e)
finally:
    client.close()
