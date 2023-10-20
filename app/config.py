from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    MODE: Literal["DEV", "TEST", "PROD"] = "DEV"

    DATABASE_HOST: str = "database"
    DATABASE_PORT: int = 5432
    DATABASE_USER: str = "postgres"
    DATABASE_PASSWORD: str = "postgres"
    DATABASE_NAME: str = "postgres"

    TEST_DATABASE_HOST: str = "database"
    TEST_DATABASE_PORT: int = 5432
    TEST_DATABASE_USER: str = "postgres"
    TEST_DATABASE_PASSWORD: str = "postgres"
    TEST_DATABASE_NAME: str = "test_db"

    POSTGRES_PASSWORD: str = "postgres"

    REDIS_BROKER_URL: str = "redis://redis:6379/0"

    NAMESPACE: str = "urn:sd-praktika:api"


@lru_cache
def get_settings() -> Settings:
    """Return setting instance."""
    return Settings()
