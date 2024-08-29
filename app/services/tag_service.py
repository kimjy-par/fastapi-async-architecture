from typing import Dict

from app.repositories.tag_repository import TagRepository
from app.services.base_service import BaseService
from app.schemas.tag_schema import TagCreateRequest
from app.models.tag import Tag


class TagService(BaseService):
    def __init__(self, tag_repository: TagRepository):
        self.tag_repository = tag_repository
        super().__init__(tag_repository)

    async def create(self, user_id: int, post_id: int, schema: TagCreateRequest) -> Tag:
        return await self.tag_repository.create(user_id, post_id, schema)

    async def list(
        self, user_id, post_id, paging_options: Dict = {}, eager: bool = False
    ):
        return await self.tag_repository.list_by_options(
            user_id, post_id, paging_options, eager
        )
