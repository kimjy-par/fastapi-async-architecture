from typing import List, Optional
from pydantic import BaseModel
from app.schemas.base_schema import BaseInfoModel


class PostSchema(BaseInfoModel):
    title: str
    content: str

    class Config:
        from_attributes = True

class PostListSchema(BaseModel):
    results: Optional[List[PostSchema]]

class InsertPostSchema(BaseModel):
    user_id: int
    title: str
    content: str

class UpdatePostSchema(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None