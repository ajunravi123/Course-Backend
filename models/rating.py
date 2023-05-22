from pydantic import BaseModel, Field


""" 

point means the rating value of a specific chapter. 

The values can be Positive/Negative. But the it should be in the range of -5 to +5

"""
class Rating(BaseModel):
    user: str
    point: int = Field(..., gt=-6, lt=6)