from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid_extensions import uuid7

from app.database import Base

if TYPE_CHECKING:
    from app.book.models.category import BookCategory


class Book(Base):
    __tablename__ = "books"

    id: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)

    title: Mapped[str]
    publish_year: Mapped[int]
    page_count: Mapped[int]
    weight: Mapped[int | None]

    category_id: Mapped[UUID] = mapped_column(ForeignKey("book_categories.id"))
    category: Mapped["BookCategory"] = relationship(back_populates="books")
