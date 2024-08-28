from fastapi import APIRouter, Depends
from dependency_injector.wiring import inject, Provide

from app.services.post_service import AsyncPostService
from app.core.container import Container

from app.schemas.post_schema import InsertPostSchema

async_router = APIRouter(prefix="/async", tags=["async"])

@async_router.get(path="/tags")
@inject
async def get_tags(
    service: AsyncPostService = Depends(Provide[Container.async_post_service])
    ):
    return await service.get_by_id(3)

@async_router.post(path="/users/posts")
@inject
async def creat_post_with_user_id(
    request: InsertPostSchema,
    service: AsyncPostService = Depends(Provide[Container.async_post_service])
    ):
    return await service.create_post(request)