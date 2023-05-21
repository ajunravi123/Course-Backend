from pymongo import MongoClient
conn = MongoClient("mongodb://localhost:27017/")
db = conn["kimo"]

#Adding index for courses
course_collection = db["course"]
course_collection.create_index("name", unique=True)
course_collection.create_index("email")
course_collection.create_index("date")

#Adding index for chapters
chapter_collection = db["chapter"]
chapter_collection.create_index("course_id")
chapter_collection.create_index("rating")
index_fields = [("name", 1), ("course_id", 1)]
chapter_collection.create_index(index_fields)