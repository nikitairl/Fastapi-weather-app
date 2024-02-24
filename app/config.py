from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    redis_url: str = Field(..., env='REDIS_URL')
    api_key: str = Field(..., env='API_KEY')

    model_config = SettingsConfigDict(env_file='.env', extra='allow')


@lru_cache
def get_settings() -> Settings:
    return Settings()
