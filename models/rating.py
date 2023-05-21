from pydantic import BaseModel

class Rating(BaseModel):
    user: str
    point: int