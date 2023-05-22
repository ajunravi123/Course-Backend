from pydantic import BaseModel, Field

class Rating(BaseModel):
    user: str
    point: int = Field(..., gt=-6, lt=6)