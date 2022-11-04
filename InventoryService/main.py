from threading import Thread

import uvicorn
from fastapi import FastAPI

from infrastructure.app_factory import create_app
from infrastructure.event_handler import InventoryEventHandler
from time import sleep

app: FastAPI
app, events = create_app()
rabbit_process: InventoryEventHandler


@app.on_event("startup")
async def startup_event():
    global rabbit_process
    # rabbit_process = InventoryEventHandler(rabbit, events)
    rabbit_process = InventoryEventHandler(events)
    rabbit_process.start()


@app.on_event("shutdown")
async def shutdown_event():
    global rabbit_process
    rabbit_process.stop()


if __name__ == '__main__':
    # rabbit_process = InventoryEventHandler(events)
    # rabbit_process.start()
    uvicorn.run('main:app', host='0.0.0.0', port=8003, reload=True)
