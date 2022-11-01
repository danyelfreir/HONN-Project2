from fastapi import FastAPI
import presentation.endpoints as buyer_endpoints
from infrastructure.container import Container
from infrastructure.settings import Settings
from persistence.reset_db import *


def create_app() -> FastAPI:
    settings = Settings("./infrastructure/.env")
    container = Container()
    container.config.from_pydantic(settings)
    container.wire([buyer_endpoints])
    app = FastAPI()
    app.container = container
    app.include_router(buyer_endpoints.router)

    return app
