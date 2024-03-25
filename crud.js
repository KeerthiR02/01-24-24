
db.createCollection("users")

#to insert a single document into a collection
db.users.insertOne({name: "Rupa", age: 25,});

 #to insert multiple documents into a collection
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
  {title: "The Developer Hub"}, 
  {$set: {topics: ["databases", "MongoDB", "MongoDB Compass"]}}, 
  {upsert: true} 
);

#count
db.trips.countDocuments();
db.trips.countDocuments({tripduration: {$gt: 200}, usertype: "Subscriber"});

#findandModify
db.podcasts.findAndModify({
  query: {_id: ObjectId("65c45e54c6d23febaede0df0")},
  update: {$inc: {downloads: 1}},
  new: true,
});

#push.js
db.podcasts.updateOne(
  {_id: ObjectId("65c3b31c5f2b7a48feaa52e0")},
  {$push: {platforms: "Apple Podcast"}}
);

db.podcasts.findOne({title: "The Developer Hub"});


#replaceOne
db.books.replaceOne(
  {_id: ObjectId("65c3f41508ac0649ab5ae43b")}, 
  {
    _id: ObjectId("65c3f41508ac0649ab5ae43b"),
    title: "The Art of War",
    ISBN: "978-1590302255",
    thumbnailUrl: "https://example.com/art-of-war-thumbnail.jpg",
    publicationDate: ISODate("2020-01-01T00:00:00.000Z"),
    authors: ["Sun Tzu"],
  }
);

db.books.findOne({_id: ObjectId("65c3f41508ac0649ab5ae43b")});









