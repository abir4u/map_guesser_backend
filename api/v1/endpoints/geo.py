from fastapi import APIRouter, HTTPException
from services.geo_service import geo_service

router = APIRouter()

@router.get("/distance")
async def get_distance(country_a: str, country_b: str):
    data = geo_service.get_distance_data(country_a, country_b)
    if not data:
        raise HTTPException(status_code=404, detail="Country not found")
    return data

@router.get("/countries")
async def list_countries():
    return {"countries": geo_service.get_all_countries()}
