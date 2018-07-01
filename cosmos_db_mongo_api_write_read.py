import datetime
import pymongo
uri = "mongodb://njespcosmos1:aUVD0cTNpy2owGd8lr8w8F77NYT52CW2S3ddtPEWx1wbAg0wRmhJnmJIiOW9UPBYmzBJsPOiSeoUS67hMF4s5A==@njespcosmos1.documents.azure.com:10255/?ssl=true&replicaSet=globaldb"
client = pymongo.MongoClient(uri)
db = client.test_database
posts = db.posts
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}
post_id = posts.insert_one(post).inserted_id        
print(db.collection_names(include_system_collections=False))