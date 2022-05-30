import secrets
from typing import List, Union, Optional, Dict, Any

from pydantic import BaseSettings, AnyHttpUrl, validator, PostgresDsn


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ["http://localhost:3000"]

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: str = "fanny.db.elephantsql.com"
    POSTGRES_USER: str = "dlotllaz"
    POSTGRES_PASSWORD: str = "ZX1EQ_jItyM_KKK8pBaNvfV7k9ZaYxuJ"
    POSTGRES_DB: str = "dlotllaz"
    SQLALCHEMY_DATABASE_URI_DEV: Optional[PostgresDsn] = "postgresql://postgres:12345678@localhost:5433/dlotllaz"
    SQLALCHEMY_DATABASE_URI: Optional[
        PostgresDsn] = "postgresql://dlotllaz:ZX1EQ_jItyM_KKK8pBaNvfV7k9ZaYxuJ@fanny.db.elephantsql.com/dlotllaz"

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive: True

    MOTOR_DATABASE_URI_PRO: str = "mongodb+srv://ubuntu:255zC8r4ym8Z3qOR@cluster0.lnefx.mongodb.net/?retryWrites=true&w=majority"
    MOTOR_DATABASE_URI_DEV: str = "mongodb+srv://root:12345678@localhost/?retryWrites=true&w=majority"


settings = Settings()
