from app.schemas.base_schema import BaseInfoModel
from pydantic import BaseModel

class UserInfo(BaseModel):
    username: str
    email: str
    is_activate: bool

class UserResponse(BaseInfoModel, UserInfo): ...

class UserCreateRequest(UserInfo): ...