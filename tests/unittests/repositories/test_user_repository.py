import pytest

from app.models.user import User
from app.repositories.user_repository import UserRepository
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
