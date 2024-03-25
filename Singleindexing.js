db.student.createIndex({"class_id":550},
{
"createdCollectionAutomatically" : false,
"numIndexesBefore" : 1,
"numIndexesAfter" : 2,
"ok" : 1
} )

#to list all the indexes

db.student.getIndexes()
