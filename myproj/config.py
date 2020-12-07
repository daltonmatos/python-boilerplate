# Standard library imports
import os

# Third party imports
from pydantic import BaseSettings


class Settings(BaseSettings):
    """
        https://pydantic-docs.helpmanual.io/#settings
        Exemplo de uso das variaveis de ambiente

        REDIS_HOST: str = "localhost"
        REDIS_PORT: int = 6379
        REDIS_DATABASE: int = 0
        REDIS_URL: str = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DATABASE}"
    """

    DEBUG: bool = True

    class Config:
        env_prefix = os.getenv("NAMESPACE", "DEV").upper() + "_"


settings = Settings()
