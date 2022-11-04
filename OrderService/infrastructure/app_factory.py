from fastapi import FastAPI

import presentation.endpoints as order_endpoints
from infrastructure.container import Container
from infrastructure.settings import Settings


def create_app() -> FastAPI:
    settings = Settings("./infrastructure/.env")
    container = Container()
    container.config.from_pydantic(settings)
    container.wire([order_endpoints])

    app = FastAPI()
    app.container = container
    app.include_router(order_endpoints.router)

    return app
