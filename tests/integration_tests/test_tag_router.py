import pytest

from app.models.user import User
from app.models.post import Post
from app.models.tag import Tag
from tests.test_utils import create_user, create_post, save_to_db


@pytest.mark.asyncio(loop_scope="session")
async def test_get_tags(client):
    first_user = await create_user(
        User(username="user1", email="user1@mnc.ai", is_activate=True)
    )
    second_user = await create_user(
        User(username="user2", email="user2@mnc.ai", is_activate=True)
    )
    third_user = await create_user(
        User(username="user3", email="user3@mnc.ai", is_activate=True)
    )

    first_user_id = first_user.id
    second_user_id = second_user.id
    third_user_id = third_user.id

    first_post = await create_post(
        Post(title="title1", content="content1", user=first_user)
    )
    second_post = await create_post(
        Post(title="title2", content="content2", user=first_user)
    )

    first_post_id = first_post.id
    second_post_id = second_post.id

    await save_to_db(Tag(tag_name="my tag", user=first_user, post=first_post))
    await save_to_db(Tag(tag_name="my tag", user=second_user, post=first_post))
    await save_to_db(Tag(tag_name="my tag", user=second_user, post=first_post))

    resp = await client.get(f"/v1/tags?user_id={first_user_id}")
    result_with_first_user = resp.json()

    assert resp.status_code == 200
    assert result_with_first_user["total_count"] == 1

    resp = await client.get(f"/v1/tags?user_id={second_user_id}")
    result_with_second_user = resp.json()

    assert resp.status_code == 200
    assert result_with_second_user["total_count"] == 2

    resp = await client.get(f"/v1/tags?user_id={third_user_id}")
    result_with_third_user = resp.json()

    assert resp.status_code == 200
    assert result_with_third_user["total_count"] == 0

    resp = await client.get(f"/v1/tags?post_id={first_post_id}")
    result_with_first_post = resp.json()

    assert resp.status_code == 200
    assert result_with_first_post["total_count"] == 3

    resp = await client.get(f"/v1/tags?post_id={second_post_id}")
    result_with_first_post = resp.json()

    assert resp.status_code == 200
    assert result_with_first_post["total_count"] == 0
