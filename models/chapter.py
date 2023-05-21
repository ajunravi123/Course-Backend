from pydantic import BaseModel, Field
from typing import List, Dict
from models.rating import Rating
from bson import ObjectId
from models.objectIdConvertion import PyObjectId

class Chapter(BaseModel):
    name: str
    course_id: PyObjectId = Field(default_factory=PyObjectId, alias="course_id")
    text: str
    rating: List[Rating]


class ChaptersResponseSchema(BaseModel):
    id : str = Field(default_factory=str, alias="_id") #PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    course_id: str = Field(default_factory=str, alias="course_id") # PyObjectId = Field(default_factory=PyObjectId, alias="course_id")
    text: str
    rating: List[Rating]

class ChapterResponseSchema(BaseModel):
    id : str = Field(default_factory=str, alias="_id") #PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    course_id: str = Field(default_factory=str, alias="course_id") # PyObjectId = Field(default_factory=PyObjectId, alias="course_id")
    text: str
    rating: List[Rating]
    course_info: Dict