from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, ForeignKey
from bot.database.db import Base


class Order(Base):
    __tablename__ = 'orders'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey('clients.id'))

    client: Mapped["Client"] = relationship("Client", back_populates="orders")
