from sqlalchemy import String, Numeric
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, registry, mapped_column
from typing import Annotated
from config import settings
from decimal import Decimal

engine = create_async_engine(settings.DATABASE_URL)

async_session_maker = async_sessionmaker(
    bind=engine, expire_on_commit=False)

str30 = Annotated[str, 30]
num10_2 = Annotated[Decimal, 10]
intpk = Annotated[int, mapped_column(primary_key=True)]


class Base(DeclarativeBase):
    registry = registry(
        type_annotation_map={
            str30: String(30),
            num10_2: Numeric(10, 2),
        }
    )
