from fastapi import FastAPI
from api.v1.api import api_router
from core.config import settings

app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Include the main hub
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == "__main__":
    import uvicorn
    # Use string-based loading for the reload feature to work correctly
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
