from typing import AsyncGenerator
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from app.core.config import settings


engine = create_async_engine(settings.database_url, echo=True)

async_session_factory = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False, autoflush=False)

async def getdb() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_factory() as session:
        yield session
