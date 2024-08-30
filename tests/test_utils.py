from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.future import select
from sqlalchemy.sql import text

from app.core.config import configs
from app.models.user import User
from app.models.post import Post


engine = create_async_engine(configs.DB_URL)


async def insert_data():
    user_list = [
        {"username": "kimjy1", "email": "kimjy1@mnc.ai", "is_activate": True},
        {"username": "kimjy2", "email": "kimjy2@mnc.ai", "is_activate": True},
        {"username": "kimjy3", "email": "kimjy3@mnc.ai", "is_activate": True},
    ]

    users = [await create_user(User(**user)) for user in user_list]


async def create_user(user):
    async with AsyncSession(engine) as session:
        session.add(user)
        await session.commit()
        await session.refresh(user)
        return user


async def create_post(post):
    async with AsyncSession(engine) as session:
        session.add(post)
        await session.commit()
        await session.refresh(post)
        return post


async def save_to_db(model):
    async with AsyncSession(engine) as session:
        session.add(model)
        await session.commit()
        await session.refresh(model)
        return model


async def delete_all_records():
    await delete_all_users()
    await delete_all_posts()


async def delete_all_users():
    async with AsyncSession(engine) as session:
        await session.execute(text("DELETE FROM users"))
        await session.commit()


async def delete_all_posts():
    async with AsyncSession(engine) as session:
        await session.execute(text("DELETE FROM posts"))
        await session.commit()
