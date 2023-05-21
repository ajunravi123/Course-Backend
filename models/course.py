from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Dict
from models.chapter import Chapter, ChaptersResponseSchema
from models.objectIdConvertion import PyObjectId

class Course(BaseModel):
    name: str
    date: datetime
    description: str
    domain: List[str]
    overall_rating: int

class CourseResponseSchema(BaseModel):
    id: str = Field(default_factory=str, alias="_id") # PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    date: datetime
    description: str
    domain: List[str]
    overall_rating: int
    chapters: List[ChaptersResponseSchema]