from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, status

from app.services.post_service import PostService
from app.core.container import Container
from app.schemas.post_schema import (
    PostListResponse,
    PostResponse,
    PostWithUserResponse,
    PostUpdateRequest,
    PostCreateRequest,
)

router = APIRouter(prefix="/v1/posts", tags=["posts"])


@router.get(path="", response_model=PostListResponse)
@inject
async def get_posts(service: PostService = Depends(Provide[Container.post_service])):
    return await service.list(eager=True)


@router.get(path="/{post_id}", response_model=PostWithUserResponse)
@inject
async def get_post_by_id(
    post_id: int, service: PostService = Depends(Provide[Container.post_service])
):
    return await service.read_by_id(post_id, eager=True)


@router.patch(path="/{post_id}", response_model=PostResponse)
@inject
async def update_post(
    post_id: int,
    request: PostUpdateRequest,
    service: PostService = Depends(Provide[Container.post_service]),
):
    return await service.update_by_id(post_id, request)


@router.post(path="", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
@inject
async def create_post(
    user_id: int,
    request: PostCreateRequest,
    service: PostService = Depends(Provide[Container.post_service]),
):
    return await service.create(user_id, request)


@router.delete(path="/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_post(
    post_id: int, service: PostService = Depends(Provide[Container.post_service])
):
    return await service.delete_by_id(post_id)
