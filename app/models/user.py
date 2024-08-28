from typing import List

from sqlalchemy import String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True)
    is_activate: Mapped[bool] = mapped_column(Boolean, nullable=False)