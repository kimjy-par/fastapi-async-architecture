from contextlib import AbstractAsyncContextManager
from typing import Callable
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload
from sqlalchemy.future import select
from app.models.post import Post
from app.models.user import User
from app.repositories.base_repository import BaseRepository
from app.schemas.post_schema import PostCreateRequest
from app.core.exceptions import NotFoundError


class PostRepository(BaseRepository):
    def __init__(
        self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]]
    ):
        self.session_factory = session_factory
        super().__init__(session_factory, Post)

    async def create_with_user_id(
        self, user_id: int, schema: PostCreateRequest
    ) -> Post:
        async with self.session_factory() as session:
            user = await session.execute(select(User).where(User.id == user_id))
            user = user.scalars().first()

            model = self.model(**schema.model_dump())
            model.user = user

            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model
