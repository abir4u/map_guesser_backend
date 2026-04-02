from contextlib import asynccontextmanager

from fastapi import FastAPI
from motor.motor_asyncio import AsyncIOMotorClient
from api.v1.api import api_router
from core.config import settings
from db.mongodb import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.client = AsyncIOMotorClient(settings.MONGO_URI)
    print("Connected to MongoDB")

    yield

    db.client.close()
    print("Disconnected from MongoDB")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    lifespan=lifespan
)

app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    # Use string-based loading for the reload feature to work correctly
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
