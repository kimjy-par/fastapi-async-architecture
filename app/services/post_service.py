from typing import List
from app.models.post import Post
from app.repositories.post_repository import PostRepository
from app.schemas.post_schema import InsertPostSchema, UpdatePostSchema


class PostService():
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    def get_all_by_user_id(self, user_id: int) -> List[Post]:
        posts =  self.post_repository.get_all_by_user_id(user_id)
        print(posts)
        return posts
    
    def create_post_by_tag(self, schema: InsertPostSchema):
        post = Post(**schema.dict())
        self.post_repository.create_post_with_user(post)
        return post
    
    def update_post(self, post_id, schema: UpdatePostSchema):
        return self.post_repository.update_post(post_id, schema)
    
    def delete_post(self, post_id):
        return self.post_repository.delete_post(post_id)
    

class AsyncPostService():
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository

    async def get_by_id(self, id: int) -> Post:
        post = await self.post_repository.get_by_id(id)
        return post
    
    async def create_post(self, schema: InsertPostSchema):
        post = Post(**schema.model_dump())
        return await self.post_repository.create_post_with_user(post)