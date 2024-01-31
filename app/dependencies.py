from collections.abc import AsyncGenerator

from motor.core import AgnosticClientSession, AgnosticDatabase

from app.database import client


async def get_session() -> AsyncGenerator[AgnosticClientSession, None]:
    async with await client.start_session() as session:
        yield session


async def get_database() -> AsyncGenerator[AgnosticDatabase, None]:
    yield client.mongo
