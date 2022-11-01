from pydantic import BaseSettings


class Settings(BaseSettings):
    postgres_host: str
    postgres_user: str
    postgres_password: str
    postgres_database: str

    class Config:
        env_file_encoding = "utf-8"
