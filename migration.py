import json
from pymongo.errors import PyMongoError
from models.course import Course 
from models.chapter import Chapter
from config.db import conn 

FILE_PATH = "data/courses.json"

# Loading the course information
with open(FILE_PATH, 'r') as file:
    json_data = json.load(file)

    # Iterate over Courses
    for item in json_data:
        try:
            #Course Insertion
            name = item['name']
            course_instance = Course.parse_obj({**item, "overall_rating": 0})
            result1 = conn.kimo.course.insert_one(dict(course_instance))
            course_id = result1.inserted_id
            chapters = item["chapters"]

            #Chapters insertion
            new_chapter_info = [dict(Chapter.parse_obj({**item, "course_id": str(course_id)})) for item in chapters]
            result = conn.kimo.chapter.insert_many(new_chapter_info)
            print(f"Course '{course_instance.name}' is inserted into the system")
        except PyMongoError as e:
            print("An error occurred:", str(e))
