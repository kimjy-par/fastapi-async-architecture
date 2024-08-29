from typing import List, Optional
from pydantic import BaseModel
from app.schemas.base_schema import BaseInfoModel, BaseList
from app.schemas.user_schema import UserResponse


class PostInfo(BaseModel):
    title: str
    content: str


class PostResponse(BaseInfoModel, PostInfo): ...


class PostWithUserResponse(PostResponse):
    user: UserResponse


class PostListResponse(BaseList):
    results: Optional[List[PostInfo]]


class PostCreateRequest(PostInfo): ...


class PostUpdateRequest(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
