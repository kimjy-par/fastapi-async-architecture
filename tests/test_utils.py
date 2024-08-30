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

    second_user = users[1]
    third_user = users[2]
    post_list = [
        {
            "title": "post title 1",
            "content": "post content 1",
            "user_id": second_user.id,
        },
        {
            "title": "post title 2",
            "content": "post content 2",
            "user_id": second_user.id,
        },
        {
            "title": "post title 3",
            "content": "post content 3",
            "user_id": second_user.id,
        },
        {
            "title": "post title 4",
            "content": "post content 4",
            "user_id": second_user.id,
        },
        {
            "title": "post title 5",
            "content": "post content 5",
            "user_id": second_user.id,
        },
        {
            "title": "post title 6",
            "content": "post content 6",
            "user_id": third_user.id,
        },
        {
            "title": "post title 7",
            "content": "post content 7",
            "user_id": third_user.id,
        },
        {
            "title": "post title 8",
            "content": "post content 8",
            "user_id": third_user.id,
        },
        {
            "title": "post title 9",
            "content": "post content 9",
            "user_id": third_user.id,
        },
        {
            "title": "post title 10",
            "content": "post content 10",
            "user_id": third_user.id,
        },
        {
            "title": "post title 11",
            "content": "post content 11",
            "user_id": third_user.id,
        },
    ]

    #await create_post(Post(**post_list[0]))


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