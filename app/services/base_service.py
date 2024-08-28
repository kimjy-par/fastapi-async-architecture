from typing import Any, Protocol
from pydantic import BaseModel


class RepositoryProtocol(Protocol):
    async def read_by_id(self, id: int) -> Any: ...
    async def create(self, schema: Any) -> Any: ...


class BaseService:
    def __init__(self, repository: RepositoryProtocol) -> None:
        self._repository = repository

    async def read_by_id(self, id: int) -> Any:
        return await self._repository.read_by_id(id)
    
    async def create(self, schema: BaseModel) -> Any:
        return await self._repository.create(schema)