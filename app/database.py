from motor import motor_asyncio

from app.config import get_settings

settings = get_settings()
DATABASE_URL = (
    f"mongodb://{settings.MONGO_USER}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}",
)

client = motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
