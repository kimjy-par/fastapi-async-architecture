import asyncio

from contextlib import AbstractAsyncContextManager, asynccontextmanager
from typing import AsyncGenerator, Any

from sqlalchemy import orm
from sqlalchemy.ext.asyncio import (
    create_async_engine,
    async_scoped_session,
    AsyncSession,
)


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_async_engine(db_url, echo=True)

        self._session_factory = async_scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine,
                class_=AsyncSession,
            ),
            scopefunc=asyncio.current_task,
        )

    @asynccontextmanager
    async def session(
        self,
    ) -> AsyncGenerator[Any, AbstractAsyncContextManager[AsyncSession]]:
        async_session: AsyncSession = self._session_factory()
        try:
            yield async_session
        except:
            await async_session.rollback()
            raise
        finally:
            await async_session.close()