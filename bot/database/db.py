from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from config import settings

engine = create_async_engine(settings.DATABASE_URL, echo=True)
session_maker = async_sessionmaker(engine)


class Base(DeclarativeBase):
    pass
