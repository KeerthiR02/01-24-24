#to create a new collection
db.createCollection("users")

#create_operation to insert a single document into a collection
db.users.insertOne({name: "Rupa", age: 25,});

#create_operation to insert multiple documents into a collection
db.users.insertMany([
    {
        name: "Rupa",
        age: 25,
    },
    {
        name: "Anitha",
        age: 30,
        
    },
    {
        name: "Kavya",
        age: 24,
    }
]);

#read_operations
#to retrieve data from a collection we use find() method
db.users.find()

#to retrieve a single document object
db.users.findOne({ name: "Kavya" })

#update_operations
#to update single document
db.users.updateOne({ name: "Kavya" }, { $set: { email: "kavya@gmail.com" } })

#to update multiple documents
db.users.updateMany({ age: { $lt: 30 } }, { $set: { status: "active" } })

#delete_operations
#to remove a single document
db.users.deleteOne({ name: "Anitha" })

#to remove multiple documnets
db.users.deleteMany({ age: { $lt: 30 } })

#updateOne
db.podcasts.updateOne(
  {title: "The Developer Hub"}, // Specify the query to find the document by its title
  {$set: {topics: ["databases", "MongoDB", "MongoDB Compass"]}}, 
  {upsert: true} 
);

#count.js for counting trip duration
db.trips.countDocuments();
db.trips.countDocuments({tripduration: {$gt: 200}, usertype: "Subscriber"});


