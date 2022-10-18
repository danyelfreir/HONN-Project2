from fastapi import FastAPI

app = FastAPI()
BASE_URL = '/api/v1/buyer'

@app.get(f'{BASE_URL}/')
async def root():
	return {'message': 'Hello from Buyer Service!'}