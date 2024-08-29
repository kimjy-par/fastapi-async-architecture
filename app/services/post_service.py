from app.services.base_service import BaseService
from app.repositories.post_repository import PostRepository
from app.schemas.post_schema import PostCreateRequest
from app.models.post import Post


class PostService(BaseService):
    def __init__(self, post_repository: PostRepository):
        self.post_repository = post_repository
        super().__init__(post_repository)

    async def create(self, user_id: int, schema: PostCreateRequest) -> Post:
        return await self.post_repository.create_with_user_id(user_id, schema)
