from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.models.base_model import BaseModel
from app.models.user import User


class Post(BaseModel):
    __tablename__ = "posts"

    user_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("users.id"), nullable=False
    )
    title: Mapped[str] = mapped_column(String, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="posts")
    tags: Mapped[list["Tag"]] = relationship("Tag", back_populates="post")
