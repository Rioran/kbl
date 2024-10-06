from datetime import datetime

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .model_base import Base


class Key(Base):
    __tablename__ = 'keys'

    id: Mapped[int] = mapped_column(primary_key=True)

    layout_id: Mapped[int] = mapped_column(ForeignKey('layouts.id'))
    layout: Mapped['Layout'] = relationship(back_populates='keys')

    us_key: Mapped[str] = mapped_column()
    remap_key: Mapped[str] = mapped_column()

    created: Mapped[datetime] = mapped_column(server_default=func.now())
    updated: Mapped[datetime] = mapped_column(server_default=func.now())

    def __repr__(self):
        return f'<Key {self.id}: remap {self.us_key} to {self.remap_key}>'
