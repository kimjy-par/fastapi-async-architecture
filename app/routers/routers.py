from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.services.user_service import UserService
from app.core.container import Container
from app.schemas.user_schema import UserResponse, UserCreateRequest
from app.schemas.post_schema import PostSchema, PostListSchema, UpdatePostSchema, InsertPostSchema

router = APIRouter(prefix="/v1", tags=["v1"])

@router.get(path="/users/{user_id}", response_model=UserResponse)
@inject
async def get_user_by_id(user_id: int, service: UserService = Depends(Provide[Container.user_service])) -> UserResponse:
    return await service.read_by_id(user_id)

@router.post(path="/users")
@inject
async def create_user(request: UserCreateRequest, service: UserService = Depends(Provide[Container.user_service])) -> UserResponse:
    return await service.create(request)

