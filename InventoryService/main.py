from threading import Thread

import uvicorn
from fastapi import FastAPI

from infrastructure.app_factory import create_app
from infrastructure.event_handler import InventoryEventHandler
from time import sleep

app: FastAPI
app, events, rabbit = create_app()



def thread_function(name):

    print('hello world')
    sleep(2)

@app.on_event("startup")
async def startup_event():
    rabbit_process = InventoryEventHandler(rabbit, events)
    rabbit_process.start()


if __name__ == '__main__':
    print('whwat')
    # sleep(100)
    uvicorn.run('main:app', host='0.0.0.0', port=8003, reload=True)
