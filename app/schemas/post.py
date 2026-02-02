from pydantic import BaseModel
from datetime import datetime
from .user import UserOut

class PostBase(BaseModel):
    title: str
    content: str

class PostCreate(PostBase):
    pass

class Post(PostBase):
    id: int
    content: str
    author: UserOut
    created_at: datetime
    rating: int

    class Config:
        from_attributes: True