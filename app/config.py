import dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class AuthSettings(BaseModel):
    KEY: str


class PostgresqlSettings(BaseModel):
    HOST: str
    PORT: int
    NAME: str
    USER: str
    PASSWORD: str


class MainSettings(BaseModel):
    HOST: str
    PORT: int

class Settings(BaseSettings):
    AUTH: AuthSettings
    DB: PostgresqlSettings
    MAIN: MainSettings

    model_config = SettingsConfigDict(
        env_file=dotenv.find_dotenv(".env"),
        env_nested_delimiter="_",
    )


settings = Settings()


def get_db_url():
    return (
        f"postgresql+asyncpg://{settings.DB.USER}:{settings.DB.PASSWORD}@"
        f"{settings.DB.HOST}:{settings.DB.PORT}/{settings.DB.NAME}"
    )
