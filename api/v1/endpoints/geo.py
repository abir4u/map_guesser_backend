from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from services.geo_service import get_geo_service, GeoService

router = APIRouter()

@router.get("/distance")
def get_distance(
    country_a: str,
    country_b: str,
    geo_service: GeoService = Depends(get_geo_service)
):
    return geo_service.get_distance_data(country_a, country_b)

@router.get("/countries")
async def list_countries():
    geo_service = get_geo_service()
    countries = geo_service.list_shp_countries()

    if not countries:
        raise HTTPException(status_code=500, detail="Could not load countries from shapefile")

    return {"count": len(countries), "countries": countries}

@router.get("/outline/{country_name}", responses={200: {"content": {"image/png": {}}}})
async def get_outline(country_name: str):
    geo_service = get_geo_service()
    image_buf = geo_service.get_country_outline(country_name)
    if not image_buf:
        raise HTTPException(status_code=404, detail="Country outline not found")

    return StreamingResponse(image_buf, media_type="image/png")
