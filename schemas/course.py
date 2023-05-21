def courseEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        "name":item["name"],
        "date":item["date"],
        "chapters":item["chapters"]
    }

def coursesEntity(entity) -> list:
    return [courseEntity(item) for item in entity]


def chapterEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "course_id":str(item["_id"]),
        "date": item["date"],
        "chapters":item["chapters"]
    }

def chaptersEntity(entity) -> list:
    return [chapterEntity(item) for item in entity]

def serializeDict(a) -> dict:
    resp = {}
    possible_object_fields = ["_id", "course_id", "id"]
    for key, value in a.items():
        if key in possible_object_fields:
            value = str(value)
        resp[key] = value
    return resp
    
    # return {**{i:str(a[i]) for i in a if i=='_id' or i=='course_id'},**{i:a[i] for i in a if i!='_id' or i!='course_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]