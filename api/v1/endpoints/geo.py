from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
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

@router.get("/outline/{country_name}", responses={200: {"content": {"image/png": {}}}})
async def get_outline(country_name: str):
    image_buf = geo_service.get_country_outline(country_name)
    if not image_buf:
        raise HTTPException(status_code=404, detail="Country outline not found")

    return StreamingResponse(image_buf, media_type="image/png")
