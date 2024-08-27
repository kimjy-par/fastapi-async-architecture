from app.schemas.base_schema import BaseInfoModel

class UserResponseSchema(BaseInfoModel):
    username: str
    email: str