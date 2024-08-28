from typing import Any, Protocol, TypeVar, Type
from app.models.base_model import BaseModel


class RepositoryProtocol(Protocol):
    async def read_by_id(self, id: int) -> Any: ...
    async def create(self, schema: Any) -> Any: ...
    async def update_by_id(self, id:int, schema: Any) -> Any: ...
    async def delete_by_id(self, id:int, schema: Any) -> Any: ...


class BaseService:
    def __init__(self, repository: RepositoryProtocol) -> None:
        self._repository = repository

    async def read_by_id(self, id: int) -> Any:
        return await self._repository.read_by_id(id)
    
    async def create(self, schema: Any) -> Any:
        return await self._repository.create(schema)
    
    async def update_by_id(self, id: int, schema: Any) -> Any:
        return await self._repository.update_by_id(id, schema)
    
    async def delete_by_id(self, id: int) -> None:
        return await self._repository.delete_by_id(id)
    