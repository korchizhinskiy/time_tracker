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

    POSTGRES_PASSWORD: str = "postgres"


@lru_cache
def get_settings() -> Settings:
    """Return setting instance."""
    return Settings()
