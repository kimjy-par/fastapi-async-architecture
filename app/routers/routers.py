from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from app.services.user_service import UserService
from app.services.post_service import PostService, AsyncPostService
from app.core.container import Container
from app.schemas.user_schema import UserResponseSchema
from app.schemas.post_schema import PostSchema, PostListSchema, UpdatePostSchema, InsertPostSchema

router = APIRouter(prefix="/v1", tags=["v1"])

@router.get(path="/users")
async def get_users():
    return {"user": "me"}

@router.get(path="/users/{user_id}", response_model=UserResponseSchema)
@inject
def get_user_by_id(user_id: int, service: UserService = Depends(Provide[Container.user_service])) -> UserResponseSchema:
    return service.get_by_id(user_id)

@router.get(path="/users/{user_id}/posts", response_model=PostListSchema)
@inject
def get_all_post_by_user_id(user_id: int, service: PostService = Depends(Provide[Container.post_service])) -> PostListSchema:
    print(service)
    return service.get_all_by_user_id(user_id)

@router.post(path="/users/posts")
@inject
def create_post_with_user_id(
        request: InsertPostSchema, 
        service: PostService = Depends(Provide[Container.post_service])
    ) -> PostSchema:
    return service.create_post_by_tag(request) 

@router.patch(path="/users/posts/{post_id}")
@inject
def update_post_with_post_id(
    post_id: int,
    request: UpdatePostSchema,
    service: PostService = Depends(Provide[Container.post_service])
) -> PostSchema:
    
    return service.update_post(post_id, request)

@router.delete(path="/users/posts/{post_id}")
@inject
def delete_post_by_id(
    post_id: int,
    service: PostService = Depends(Provide[Container.post_service])
):
    return service.delete_post(post_id)
