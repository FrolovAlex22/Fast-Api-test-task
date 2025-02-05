from datetime import datetime
from enum import Enum as PyEnum

from sqlalchemy import (
    Enum,
    ForeignKey,
    String,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(
        index=True, server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        index=True, server_default=func.now(), onupdate=func.now()
    )


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), nullable=False)
    password_hash: Mapped[str] = mapped_column(String(70), nullable=False)
