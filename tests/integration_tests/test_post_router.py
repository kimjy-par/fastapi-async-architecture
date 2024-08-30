import pytest

from app.models.user import User
from app.models.post import Post
from sqlalchemy.future import select
from tests.test_utils import create_user, create_post

@pytest.mark.asyncio(loop_scope="session")
async def test_get_posts(client):
    resp = await client.get('/v1/posts')
    assert resp.status_code == 200


@pytest.mark.asyncio(loop_scope="session")
async def test_get_post_by_id(client):
    user = User(username="post_user", email="post_user@mnc.ai", is_activate=True)
    user = await create_user(user)
    user_id = user.id
    
    post = Post(title="post title", content="post_content", user=user)
    post = await create_post(post)

    resp = await client.get(f"/v1/posts/{post.id}")
    post_from_resp = resp.json()

    assert resp.status_code == 200
    assert post_from_resp["id"] == post.id
    assert post_from_resp["title"] == post.title
    assert post_from_resp["content"] == post.content
    assert post_from_resp["user"]["id"] == user_id

@pytest.mark.asyncio(loop_scope="session")
async def test_create_post(client, session):
    user = User(username="post_user", email="post_user@mnc.ai", is_activate=True)
    user = await create_user(user)
    user_id = user.id

    resp = await client.post(f"/v1/posts?user_id={user_id}", json={"title": "title for test", "content": "content for test"})
    post_from_resp = resp.json()

    post = await session.execute(select(Post).where(Post.id==post_from_resp["id"]))
    post = post.scalars().first()
    
    assert resp.status_code == 201

    assert post.title == "title for test"
    assert post.content == "content for test"


@pytest.mark.asyncio(loop_scope="session")
async def test_update_post(client, session):
    user = User(username="post_user", email="post_user@mnc.ai", is_activate=True)
    user = await create_user(user)
    post = Post(title="post title", content="post_content", user=user)
    post = await create_post(post)

    resp = await client.patch(f"/v1/posts/{post.id}", json={"title":"title to change", "content": "content to change"})

    post = await session.execute(select(Post).where(Post.id==post.id))
    post = post.scalars().first()

    assert resp.status_code == 200

    assert post.title == "title to change"
    assert post.content == "content to change"


@pytest.mark.asyncio(loop_scope="session")
async def test_delete_post(client, session):
    user = User(username="post_user", email="post_user@mnc.ai", is_activate=True)
    user = await create_user(user)
    post = Post(title="post title", content="post_content", user=user)
    post = await create_post(post) 

    resp = await client.delete(f"/v1/posts/{post.id}")

    post = await session.execute(select(Post).where(Post.id==post.id))
    post = post.scalars().first()

    assert resp.status_code == 204
    assert post is None
