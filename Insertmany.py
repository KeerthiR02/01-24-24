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