from fastapi import FastAPI
from api.v1.endpoints import geo

app = FastAPI(title="Geo API", version="1.0.0")

# Include the routers
app.include_router(geo.router, prefix="/api/v1/geo", tags=["Geography"])

# When you add auth later, it's just one line:
# app.include_router(auth.router, prefix="/api/v1/auth", tags=["Security"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
