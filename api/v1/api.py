from fastapi import APIRouter
from api.v1.endpoints import geo, auth

api_router = APIRouter()

api_router.include_router(geo.router, prefix="/geo", tags=["Geography"])
api_router.include_router(auth.router, prefix="/auth", tags=["Authentication"])
