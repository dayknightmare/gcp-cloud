from src.routers.os_info import os_info_route
from fastapi import FastAPI
import uuid


app = FastAPI(
    description="Google Cloud Platform demonstration application with load balancing",
    title="GCP DEMO APP",
    version='1.1.1'
)

app.include_router(os_info_route)

@app.on_event('startup')
async def startup():
    app.state.uuid = str(uuid.uuid4())