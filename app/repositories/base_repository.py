from contextlib import AbstractAsyncContextManager
from typing import Callable, Type, TypeVar
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.base_model import BaseModel

T = TypeVar("T", bound=BaseModel)

class BaseRepository:
    def __init__(self, session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]], model: Type[T]):
        self.session_factory = session_factory
        self.model = model

    async def get_by_id(self, id: int) -> T:
        async with self.session_factory() as session:
            query = await session.execute(select(self.model).filter(self.model.id==id))
            return query.scalars().first()
        
    async def create(self, schema: T):
        async with self.session_factory() as session:
            session.add(schema)
            await session.commit()
            return await session.refresh(schema)