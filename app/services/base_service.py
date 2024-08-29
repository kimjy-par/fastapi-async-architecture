from typing import Any, Protocol, TypeVar, Type, List, Dict
from app.models.base_model import BaseModel


class RepositoryProtocol(Protocol):
    async def read_by_id(self, id: int, eager: bool) -> Any: ...
    async def list(self, paging_options, eager: bool) -> Any: ...
    async def list_by_query(self, query, paging_options, eager: bool) -> Any: ...
    async def create(self, schema: Any) -> Any: ...
    async def update_by_id(self, id: int, schema: Any) -> Any: ...
    async def delete_by_id(self, id: int, schema: Any) -> Any: ...


class BaseService:
    def __init__(self, repository: RepositoryProtocol) -> None:
        self._repository = repository

    async def read_by_id(self, id: int) -> Any:
        return await self._repository.read_by_id(id)

    async def list(self, paging_options: Dict = {}, eager: bool = False):
        return await self._repository.list(paging_options, eager)

    async def create(self, schema: Any) -> Any:
        return await self._repository.create(schema)

    async def update_by_id(self, id: int, schema: Any) -> Any:
        return await self._repository.update_by_id(id, schema)

    async def delete_by_id(self, id: int) -> None:
        return await self._repository.delete_by_id(id)
