from typing import List, Union

from pydantic import (
    BaseSettings, validator, AnyHttpUrl, PostgresDsn, RedisDsn, Field
)


class AppSettings(BaseSettings):
    SERVICE_NAME: str = "FastApi Template"
    SERVER_NAME: str = "DEV"
    DEBUG: bool = True
    SECRET_KEY: str = "=%m=#x49tt#csz=s!u1d%08o1j0(t1de(1-(vqe_ojy05$^v=^"
    JWT_SECRET: str = SECRET_KEY
    JWT_LIFETIME: int = 3600
    DATABASE_URI: PostgresDsn = Field(
        env="DATABASE_URI", default="postgresql+asyncpg://psql:psql@127.0.0.1:5432/psql"
    )
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    SENTRY_SDN: str = None
    # REDIS_DSN: RedisDsn

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[
        List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "app_"


settings = AppSettings()
