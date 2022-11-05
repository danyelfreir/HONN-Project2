from threading import Thread

import uvicorn
from fastapi import FastAPI

from infrastructure.app_factory import create_app
from infrastructure.event_handler import InventoryEventHandler
from presentation.events import Events

app: FastAPI
events: Events
app, events = create_app()


def start_handler():
    rabbit = InventoryEventHandler(events)
    rabbit.run()


@app.on_event("startup")
async def startup_event():
    rabbit_process = Thread(target=start_handler, daemon=True)
    rabbit_process.start()


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8003, reload=True)
