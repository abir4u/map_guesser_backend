from fastapi import APIRouter
from api.v1.endpoints import geo
# from app.api.v1.endpoints import auth  # You'll uncomment this when you add auth

api_router = APIRouter()

# Here we "glue" the specific feature routers to the main v1 router
api_router.include_router(geo.router, prefix="/geo", tags=["Geography"])

# Future features would go here:
# api_router.include_router(auth.router, prefix="/auth", tags=["Security"])
