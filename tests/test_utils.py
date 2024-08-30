from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import text

from app.core.config import configs
from app.models.user import User


engine = create_async_engine(configs.DB_URL)


async def create_users():
    user_list = [
        {"username": "kimjy1", "email": "kimjy1@mnc.ai", "is_activate": True},
        {"username": "kimjy2", "email": "kimjy2@mnc.ai", "is_activate": True},
        {"username": "kimjy3", "email": "kimjy3@mnc.ai", "is_activate": True},
    ]

    [await create_user(User(**user)) for user in user_list]


async def create_user(user):
    async with AsyncSession(engine) as session:
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


async def delete_all_records():
    async with AsyncSession(engine) as session:
        await session.execute(text("DELETE FROM users"))
        await session.commit()
