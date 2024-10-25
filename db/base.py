from contextlib import asynccontextmanager
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncAttrs, AsyncSession, create_async_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

from utils import config

# Create an asynchronous engine
engine = create_async_engine(
    config.SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False,
)

# Create an asynchronous session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)


class Base(DeclarativeBase, AsyncAttrs):
    # Define a base class for declarative models
    pass


@asynccontextmanager
async def GetDB() -> AsyncGenerator[AsyncSession, None]:
    """
    Provide an asynchronous database session to the application.
    """
    async with AsyncSessionLocal() as session:
        yield session
