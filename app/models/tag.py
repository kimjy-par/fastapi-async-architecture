from typing import List

from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base_model import BaseModel


class Tag(BaseModel):
    __tablename__ = "tags"

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )
    post_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("posts.id"), nullable=False
    )
    tag_name: Mapped[str] = mapped_column(String, nullable=False)

    post: Mapped["Post"] = relationship("Post", back_populates="tags")
    user: Mapped["User"] = relationship("User", back_populates="tags")
