from typing import Any, Protocol

class RepositoryProtocol(Protocol):
    async def get_by_id(self, id: int) -> Any: ...
    async def create(self, schema: Any) -> Any: ...


class BaseService:
    def __init__(self, repository: RepositoryProtocol) -> None:
        self._repository = repository

    async def get_by_id(self, id: int) -> Any:
        return await self._repository.get_by_id(id)
    
    async def create(self, schema: Any) -> Any:
        return await self._repository.create(schema)