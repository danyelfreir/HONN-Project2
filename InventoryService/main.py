from fastapi import FastAPI

app = FastAPI()
BASE_URL = '/api/v1/inventory'

@app.get(f'{BASE_URL}/')
async def root():
	return {'message': 'Hello from Inventory Service!'}