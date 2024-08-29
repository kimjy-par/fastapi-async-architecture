from fastapi import APIRouter, Depends, status
from dependency_injector.wiring import Provide, inject

from app.core.container import Container
from app.services.tag_service import TagService

from app.schemas.tag_schema import (
    TagResponse,
    TagWithUserPostResponse,
    TagCreateRequest,
    TagUpdateRequest,
    TagListWIthUserPostResponse,
)

router = APIRouter(prefix="/v1/tags", tags=["tags"])


@router.get(path="", response_model=TagListWIthUserPostResponse)
@inject
async def get_tags(
    user_id: int = None,
    post_id: int = None,
    tag_service: TagService = Depends(Provide[Container.tag_service]),
):
    return await tag_service.list(user_id, post_id, eager=True)


@router.get(path="/{tag_id}", response_model=TagWithUserPostResponse)
@inject
async def get_tag_by_id(
    tag_id: int, tag_service: TagService = Depends(Provide[Container.tag_service])
):
    return await tag_service.read_by_id(tag_id, eager=True)


@router.post(path="")
@inject
async def create_tag(
    user_id: int,
    post_id: int,
    request: TagCreateRequest,
    tag_service: TagService = Depends(Provide[Container.tag_service]),
):
    return await tag_service.create(user_id, post_id, request)


@router.patch(path="/{tag_id}")
@inject
async def update_tag(
    tag_id: int,
    request: TagUpdateRequest,
    tag_service: TagService = Depends(Provide[Container.tag_service]),
):
    return await tag_service.update_by_id(tag_id, request)


@router.delete(path="/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
@inject
async def delete_tag(
    tag_id: int, tag_service: TagService = Depends(Provide[Container.tag_service])
):
    return await tag_service.delete_by_id(tag_id)
