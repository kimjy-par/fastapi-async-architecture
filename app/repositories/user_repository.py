from contextlib import AbstractContextManager
from typing import Callable
from sqlalchemy.orm import Session

from app.models.user import User

class UserRepository():
    def __init__(self, session_factory: Callable[..., AbstractContextManager[Session]]):
        self.session_factory = session_factory

    def get_by_id(self, id: int) -> User:
        with self.session_factory() as session:
            query = session.query(User).filter(User.id == id).first()
           
            if not query:
                raise 

            return query