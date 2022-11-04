from fastapi import FastAPI
import presentation.endpoints as api_endpoints

def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(api_endpoints.router)
    return app

