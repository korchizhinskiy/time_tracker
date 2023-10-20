from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, async_sessionmaker, create_async_engine

from app.celery import settings

if settings.MODE == "TEST":
    DATABASE_URL = (
        f"postgresql+asyncpg://{settings.DATABASE_USER}:{settings.DATABASE_PASSWORD}@"
        f"{settings.DATABASE_HOST}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"
    )
    DATABASE_PARAMS = {"poolclass": NullPool}
else:
    DATABASE_URL = (
        f"postgresql+asyncpg://{settings.TEST_DATABASE_USER}:{settings.TEST_DATABASE_PASSWORD}@"
        f"{settings.TEST_DATABASE_HOST}:{settings.TEST_DATABASE_PORT}/{settings.TEST_DATABASE_NAME}"
    )
    DATABASE_PARAMS = {}

engine: AsyncEngine = create_async_engine(DATABASE_URL, **DATABASE_PARAMS)
async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
    autoflush=False,
    autocommmit=False,
)
