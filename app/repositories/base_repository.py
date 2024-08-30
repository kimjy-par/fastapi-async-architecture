from contextlib import AbstractAsyncContextManager
from typing import Callable, Type, TypeVar, Dict, List, Optional

from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload, class_mapper, RelationshipProperty
from sqlalchemy.sql import text
from sqlalchemy import func

from pydantic import BaseModel

from app.core.exceptions import NotFoundError
from app.models.base_model import BaseModel


T = TypeVar("T", bound=BaseModel)
PAGE = 1
PAGE_SIZE = 20
ORDER = "asc"
ORDER_COLUMN = "id"


class BaseRepository:
    def __init__(
        self,
        session_factory: Callable[..., AbstractAsyncContextManager[AsyncSession]],
        model: Type[T],
    ):
        self.session_factory = session_factory
        self.model = model

    async def read_by_id(self, id: int, eager: bool = False) -> T:
        async with self.session_factory() as session:
            query = select(self.model).filter(self.model.id == id)
            if eager:
                eager_attrs = await self._extract_relationship_attrs()
                for attr in eager_attrs:
                    query = query.options(joinedload(getattr(self.model, attr)))

            result = await session.execute(query)
            result = result.scalars().first()
            if not result:
                raise NotFoundError

            return result

    async def list(self, paging_options: Dict = {}, eager: bool = False) -> List[T]:
        query = select(self.model)
        return await self.list_by_query(
            query, paging_options=paging_options, eager=eager
        )

    async def list_by_query(
        self, query, paging_options: Dict = {}, eager: bool = False
    ) -> List[T]:
        async with self.session_factory() as session:
            page = paging_options.get("page", PAGE)
            page_size = paging_options.get("page_size", PAGE_SIZE)
            order_column = paging_options.get("order_column", ORDER_COLUMN)
            order = paging_options.get("order", ORDER)
            offset = (page - 1) * page_size

            total_count = await session.execute(
                select(func.count()).select_from(query.subquery())
            )
            total_count = total_count.scalar()

            if eager:
                eager_attrs = await self._extract_relationship_attrs()
                for attr in eager_attrs:
                    query = query.options(joinedload(getattr(self.model, attr)))

            results = await session.execute(
                query.offset(offset)
                .limit(page_size)
                .order_by(text(f"{order_column} {order}"))
            )
            results = results.scalars()

            return {
                "results": results,
                "page": page,
                "page_size": page_size,
                "total_count": total_count,
            }

    async def create(self, schema: BaseModel) -> T:
        async with self.session_factory() as session:
            model = self.model(**schema.model_dump())
            session.add(model)
            await session.commit()
            await session.refresh(model)
            return model

    async def update_by_id(self, id: int, schema: BaseModel) -> T:
        async with self.session_factory() as session:
            results = await session.execute(
                select(self.model).filter(self.model.id == id)
            )
            model = results.scalars().first()
            if not model:
                raise NotFoundError
            attrs = schema.model_dump(exclude_none=True)
            for attr in attrs.keys():
                setattr(model, attr, attrs[attr])
            await session.commit()
            await session.refresh(model)
            return model

    async def delete_by_id(self, id: int) -> None:
        async with self.session_factory() as session:
            results = await session.execute(
                select(self.model).filter(self.model.id == id)
            )
            model = results.scalars().first()
            if not model:
                raise NotFoundError
            await session.delete(model)
            await session.commit()

    async def _extract_relationship_attrs(self) -> List[str]:
        return [
            prop.key
            for prop in class_mapper(self.model).iterate_properties
            if isinstance(prop, RelationshipProperty)
        ]
