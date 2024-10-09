from dataclasses import dataclass
from datetime import datetime
from typing import Optional

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .model_base import Base


@dataclass
class Layout(Base):
    __tablename__ = 'layouts'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    description: Mapped[Optional[str]] = mapped_column()
    shortcut: Mapped[Optional[str]] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=False)

    created: Mapped[datetime] = mapped_column(server_default=func.now())
    updated: Mapped[datetime] = mapped_column(server_default=func.now())

    keys: Mapped[list['Key']] = relationship(back_populates='layout')

    def __repr__(self):
        return f'<Layout {self.id}: {self.name}>'
