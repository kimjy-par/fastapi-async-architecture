from typing import List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base_model import BaseModel


class User(BaseModel):
    __tablename__ = "users"
    
    username: Mapped[str] = mapped_column(String, nullable=False)
    email: Mapped[str] = mapped_column(String, unique=True)
    posts = relationship("Post", back_populates="user", lazy='joined')