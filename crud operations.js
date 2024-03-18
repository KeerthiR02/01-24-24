
db.createCollection("users")

#create_operation to insert a single document into a collection
db.users.insertOne({name: "Preethi", age: 19,});

#create_operation to insert multiple documents into a collection
db.users.insertMany([
    {
        name: "Preethi",
        age: 19,
    },
    {
        name: "Honey",
        age: 20,
        
    },
    {
        name: "Sonia",
        age: 29,
    }
]);


 #retrieve data from a collection we use find() method
db.users.find()

#to retrieve a single document object
db.users.findOne({ name: "Honey" })

#findmodify 

    db.podcasts.findAndModify({
  query: {_id: ObjectId("65c45e54c6d23febaede0df0")},
  update: {$inc: {downloads: 1}},
  new: true,
})

#update_operations
#to update single document
db.users.updateOne({ name: "Preethi" }, { $set: { email: "Preethi@gmail.com" } })

#to update multiple documents
db.users.updateMany({ age: { $lt: 28 } }, { $set: { status: "active" } })

#delete_operations
#to remove a single document
db.users.deleteOne({ name: "Honey" })

#to remove multiple documnets
db.users.deleteMany({ age: { $lt: 25 } })

#to remove an entire collection
db.users.drop()
