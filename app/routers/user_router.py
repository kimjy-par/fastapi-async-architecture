from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.services.user_service import UserService
from app.core.container import Container
from app.schemas.user_schema import (
    UserResponse,
    UserCreateRequest,
    UserUpdateRequest,
    UserListResponse,
)
from app.schemas.post_schema import (
    PostSchema,
    PostListSchema,
    UpdatePostSchema,
    InsertPostSchema,
)

router = APIRouter(prefix="/v1", tags=["v1"])


@router.get(path="/users")
@inject
async def get_users(
    service: UserService = Depends(Provide[Container.user_service]),
) -> UserListResponse:
    return await service.list(paging_options={"page_size": 5, "page": 2})


@router.get(path="/users/{user_id}", response_model=UserResponse)
@inject
async def get_user_by_id(
    user_id: int, service: UserService = Depends(Provide[Container.user_service])
) -> UserResponse:
    return await service.read_by_id(user_id)


@router.post(path="/users")
@inject
async def create_user(
    request: UserCreateRequest,
    service: UserService = Depends(Provide[Container.user_service]),
) -> UserResponse:
    return await service.create(request)


@router.patch(path="/users/{user_id}", response_model=UserResponse)
@inject
async def update_user(
    user_id: int,
    request: UserUpdateRequest,
    service: UserService = Depends(Provide[Container.user_service]),
):
    return await service.update_by_id(user_id, request)


@router.delete(path="/users/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_user(
    user_id: int, service: UserService = Depends(Provide[Container.user_service])
):
    await service.delete_by_id(user_id)
