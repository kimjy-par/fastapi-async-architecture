from typing import List, Optional
from pydantic import BaseModel
from app.schemas.base_schema import BaseInfoModel, BaseList
from app.schemas.user_schema import UserResponse
from app.schemas.post_schema import PostResponse


class TagInfo(BaseModel):
    tag_name: str


class TagResponse(BaseInfoModel, TagInfo): ...


class TagWithUserPostResponse(TagResponse):
    user: UserResponse
    post: PostResponse


class TagListWIthUserPostResponse(BaseList):
    results: Optional[List[TagWithUserPostResponse]]


class TagCreateRequest(TagInfo): ...


class TagUpdateRequest(BaseModel):
    tag_name: Optional[str]
