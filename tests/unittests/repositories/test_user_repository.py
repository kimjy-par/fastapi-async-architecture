import pytest

from sqlalchemy.future import select
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreateRequest, UserUpdateRequest
from tests.test_utils import create_user

@pytest.mark.asyncio(loop_scope="session")
async def test_read_by_id(database):

    user = await create_user(User(username="unittest_user", email="unit@test.com", is_activate=True))
    user_repository = UserRepository(database.session)

    user_from_db = await user_repository.read_by_id(user.id)

    assert user.id == user_from_db.id
    assert user.username == user_from_db.username
    assert user.email == user_from_db.email
    assert user.is_activate == user_from_db.is_activate

@pytest.mark.asyncio(loop_scope="session")
async def test_list_by_query(database):
    user_repository = UserRepository(database.session)
    user_list = [
        User(username="test1", email="test1@test.com", is_activate=True),
        User(username="test2", email="test2@test.com", is_activate=True),
        User(username="test3", email="test3@test.com", is_activate=True),
        User(username="test4", email="test4@test.com", is_activate=False),
        User(username="test5", email="test5@test.com", is_activate=False),
    ]
    
    users = [await create_user(user) for user in user_list]

    results = await user_repository.list_by_query(select(User))
    users_from_db = results['results']

    assert results['total_count'] == 5
    assert len(users_from_db) == 5

@pytest.mark.asyncio(loop_scope="session")
async def test_list_user_is_not_active(database):
    user_repository = UserRepository(database.session)
    user_list = [
        User(username="test1", email="test1@test.com", is_activate=True),
        User(username="test2", email="test2@test.com", is_activate=True),
        User(username="test3", email="test3@test.com", is_activate=True),
        User(username="test4", email="test4@test.com", is_activate=False),
        User(username="test5", email="test5@test.com", is_activate=False),
    ]
    
    users = [await create_user(user) for user in user_list]

    results = await user_repository.list_by_query(select(User).filter(User.is_activate==False))
    users_from_db = results['results']

    assert results['total_count'] == 2
    assert len(users_from_db) == 2


@pytest.mark.asyncio(loop_scope="session")
async def test_create_user(database):
    user_repository = UserRepository(database.session)
    user_schema = UserCreateRequest(username="create", email="create@test.com", is_activate=False)

    created_user = await user_repository.create(user_schema)
    user_from_db = await user_repository.read_by_id(created_user.id)

    assert user_from_db.username == "create"
    assert user_from_db.email == "create@test.com"
    assert user_from_db.is_activate == False


@pytest.mark.asyncio(loop_scope="session")
async def test_update_user(database):
    user_repository = UserRepository(database.session)
    user = await create_user(User(username="update", email="update@test.com", is_activate=False))

    schema_to_update = UserUpdateRequest(username="change", email="change@test.com", is_activate=True)
    updated_user = await user_repository.update_by_id(user.id, schema_to_update)
    user_from_db = await user_repository.read_by_id(user.id)

    assert user_from_db.id == user.id
    assert user_from_db.username == "change"
    assert user_from_db.email == "change@test.com"
    assert user_from_db.is_activate == True

@pytest.mark.asyncio(loop_scope="session")
async def test_delete_user(database):
    user_repository = UserRepository(database.session)
    user = await create_user(User(username="delete", email="delete@test.com", is_activate=True))
    await user_repository.delete_by_id(user.id)

    results = await user_repository.list_by_query(select(User).filter(User.id == user.id))

    assert results["total_count"] == 0
    assert results["results"] == []
    
