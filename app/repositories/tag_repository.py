from contextlib import AbstractAsyncContextManager
from typing import Callable, Dict

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.repositories.base_repository import BaseRepository
from app.models.tag import Tag
from app.models.user import User
from app.models.post import Post
from app.schemas.tag_schema import TagUpdateRequest, TagCreateRequest


class TagRepository(BaseRepository):
    def __init__(
        self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]
    ):
        super().__init__(session_factory, Tag)

    async def list_by_options(
        self, user_id, post_id, paging_options: Dict = {}, eager: bool = False
    ):
        query = select(Tag)
        if user_id is not None:
            query = query.join(User).filter(User.id == user_id)
        if post_id is not None:
            query = query.join(Post).filter(Post.id == post_id)

        return await self.list_by_query(query, paging_options, eager)

    async def create(self, user_id: int, post_id: int, schema: TagCreateRequest) -> Tag:
        async with self.session_factory() as session:
            user = await session.execute(select(User).where(User.id == user_id))
            user = user.scalars().first()

            post = await session.execute(select(Post).where(Post.id == post_id))
            post = post.scalars().first()

            model = self.model(**schema.model_dump())
            model.user = user
            model.post = post

            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model
