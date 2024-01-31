from functools import lru_cache
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="allow")

    MODE: Literal["DEV", "TEST", "PROD"] = "DEV"

    MONGO_HOST: str = "mongo"
    MONGO_PORT: int = 27017
    MONGO_USER: str = "mongo"
    MONGO_PASSWORD: str = "mongo"
    MONGO_NAME: str = "mongo"


@lru_cache
def get_settings() -> Settings:
    """Return setting instance."""
    return Settings()
