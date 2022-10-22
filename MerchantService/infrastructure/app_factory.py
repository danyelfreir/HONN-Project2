from fastapi import FastAPI
from infrastructure.settings import Settings
from infrastructure.container import Container
import presentation.endpoints as merchant_endpoints

def create_app() -> FastAPI:
    settings = Settings("./infrastructure/.env")
    container = Container()
    container.config.from_pydantic(settings)
    container.wire([merchant_endpoints])

    app = FastAPI()
    app.container = container
    app.include_router(merchant_endpoints.router)

    return app