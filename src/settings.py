from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    base_url: str
    username: str
    password: str
    environment: str = "dev"

    model_config = SettingsConfigDict(
        env_file=Path(__file__).resolve().parent.parent / ".env.test",
        env_file_encoding="utf-8",
    )


settings = Settings()


# print(settings.base_url)