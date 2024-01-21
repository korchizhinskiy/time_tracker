from typing import TYPE_CHECKING
from uuid import UUID

from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid_extensions import uuid7

from app.database import Base

if TYPE_CHECKING:
    from app.book.models.category import BookCategory


class Book(Base):
    __tablename__ = "book"

    uuid: Mapped[UUID] = mapped_column(primary_key=True, default=uuid7)

    title: Mapped[str]
    category: Mapped["BookCategory"] = relationship(back_populates="books")
