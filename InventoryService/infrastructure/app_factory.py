from fastapi import FastAPI
from typing import Tuple
import presentation.endpoints as inventory_endpoints
from presentation.events import Events
from infrastructure.container import Container
from infrastructure.event_handler import InventoryEventHandler
from infrastructure.rabbitmq import RabbitMQ
from infrastructure.settings import Settings


def create_app() -> Tuple[FastAPI, Events]:
    settings = Settings("./infrastructure/.env")
    container = Container()
    container.config.from_pydantic(settings)
    container.wire([inventory_endpoints])

    events = container.events_provider()

    app = FastAPI()
    app.container = container
    app.include_router(inventory_endpoints.router)

    return app, events
