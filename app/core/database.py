from contextlib import AbstractContextManager, contextmanager
from typing import Generator, Any

from sqlalchemy import create_engine, orm
from sqlalchemy.orm import Session


class Database:
    def __init__(self, db_url: str) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = orm.scoped_session(
            orm.sessionmaker(
                autocommit=False,
                autoflush=False,
                bind=self._engine
            )
        )

    @contextmanager
    def session(self) -> Generator[Any, Any, AbstractContextManager[Session]]:
        session: Session = self._session_factory()
        try:
            yield session
        except:
            session.rollback()
            raise
        finally:
            session.close()