from datetime import datetime
from typing import Optional, List, Any
from pydantic import BaseModel


class BaseInfoModel(BaseModel):
    id: int
    created_at: datetime
    updated_at: datetime


class BaseList(BaseModel):
    results: List[Any]
    page: Optional[int]
    page_size: Optional[int]
    total_count: Optional[int]
