from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.orm import mapped_column, relationship
from sqlalchemy.orm.base import Mapped
from uuid_extensions import uuid7

from app.database import Base

if TYPE_CHECKING:
    from app.book.models.book import Book


class BookCategory(Base):
    __tablename__ = "book_category"

    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)

    name: Mapped[str] = mapped_column(unique=True)

    books: Mapped[list["Book"]] = relationship(back_populates="category")
