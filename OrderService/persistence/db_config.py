from pydantic import BaseSettings


class DbConfig(BaseSettings):
    host: str
    user: str
    password: str
    database: str
