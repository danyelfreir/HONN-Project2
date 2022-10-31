import uvicorn
from fastapi import FastAPI

from infrastructure.app_factory import create_app

app: FastAPI = create_app()

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
