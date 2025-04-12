from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String
from bot.database.db import Base
from typing import List

class Client(Base):
    __tablename__ = 'clients'

    id: Mapped[int] = mapped_column(Integer,primary_key=True,autoincrement=True)
    tg_id: Mapped[int] = mapped_column(Integer)
    tg_name: Mapped[str] = mapped_column(String)

    orders: Mapped[List["Order"]] = relationship("Order", back_populates="client")