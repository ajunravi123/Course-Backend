from fastapi import APIRouter, Query, Path
from models.course import CourseResponseSchema
from models.chapter import ChapterResponseSchema
from config.db import conn 
from schemas.course import serializeDict, serializeList
from bson import ObjectId
from enum import Enum
from fastapi.responses import JSONResponse

course = APIRouter()

class SortByOptions(str, Enum):
    name = "name"
    date = "date"
    rating = "rating"

@course.get('/course')
async def list_courses(
    sort_by: SortByOptions = Query("name", description="Sort courses by name, date or rating. Default is by name."),
    domain : str = Query(None, description="Filter courses by domain name")
):
    descending_sort_for = ["date", "rating"]
    sort_order = -1 if sort_by in descending_sort_for else 1
    sort_by = "overall_rating" if sort_by=="rating" else sort_by
    
    pipeline = [
        {
            "$lookup": {
                "from": "chapter",
                "localField": "_id",
                "foreignField": "course_id",
                "as": "chapters"
            }
        },
        {
            "$sort": {
                sort_by : sort_order
            }
        }
    ]

    if domain is not None:
        pipeline.append({
            "$match": {
                "domain": {
                    "$in": [domain]
                }
            }
        })

    # Find query with join
    sorted_documents = conn.kimo.course.aggregate(pipeline)

    resp = []
    for item in sorted_documents:
        item["_id"] = str(item["_id"])
        item["chapters"] = serializeList(item["chapters"])
        new_data = dict(CourseResponseSchema.parse_obj(item))
        resp.append(new_data)

    return resp


@course.get('/course/{course_id}')
async def list_course(
    course_id : str = Path(..., description="ObjectID of the course")
):
    try:
        course = conn.kimo.course.find_one({"_id": ObjectId(course_id)})
        if course is not None:
            chapters_count = conn.kimo.chapter.count_documents({"course_id": ObjectId(course_id)})
            course["total_chapters"] = chapters_count
            return serializeDict(course)
        else:
            error_message = {"error": "Course not found"}
            return JSONResponse(content=error_message, status_code=200)
    except Exception as e:
        error_message = {"error": str(e)}
        return JSONResponse(content=error_message, status_code=400)

    
@course.get('/chapter')
async def get_chapter(
    name: str = Query("", description="Search chapters by chapter name"),
    course_id: str = Query("", description="Search chapters by courseID"),
    id: str = Query("", description="Search chapters by chapterID"),
):
    pipeline = [
        {
            "$lookup": {
                "from": "course",
                "localField": "course_id",
                "foreignField": "_id",
                "as": "course_info",
            }
        }
    ]

    filters = {}
    if name != "":
        filters["name"] = name
    
    if course_id != "":
        filters["course_id"] = ObjectId(course_id)

    if id != "":
        filters["_id"] = ObjectId(id)
        
    if filters is not None:
        pipeline.append({
            "$match": filters
        })

    # Find query with join
    sorted_documents = conn.kimo.chapter.aggregate(pipeline)

    resp = []
    for item in sorted_documents:
        item = serializeDict(item)
        item["course_info"] = serializeDict(item["course_info"][0])
        new_data = dict(ChapterResponseSchema.parse_obj(item))
        resp.append(new_data)

    return resp
    



# @course.get('/{id}')
# async def find_one_course(id):
#     return serializeDict(conn.kimo.course.find_one({"_id":ObjectId(id)}))

# @course.post('/')
# async def create_course(course: Course):
#     conn.kimo.course.insert_one(dict(course))
#     return serializeList(conn.kimo.course.find())

# @course.put('/{id}')
# async def update_course(id,course: Course):
#     conn.kimo.course.find_one_and_update({"_id":ObjectId(id)},{
#         "$set":dict(course)
#     })
#     return serializeDict(conn.kimo.course.find_one({"_id":ObjectId(id)}))

# @course.delete('/{id}')
# async def delete_course(id,course: Course):
#     return serializeDict(conn.kimo.course.find_one_and_delete({"_id":ObjectId(id)}))