import math
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import pycountry
from core.config import settings

class GeoService:
    def __init__(self):
        self.geolocator = Nominatim(
            user_agent=settings.GEO_USER_AGENT,
            timeout=settings.GEO_TIMEOUT
        )

    def get_all_countries(self):
        return sorted([c.name for c in pycountry.countries])

    def calculate_bearing(self, lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        d_lon = lon2 - lon1
        y = math.sin(d_lon) * math.cos(lat2)
        x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(d_lon)
        return (math.degrees(math.atan2(y, x)) + 360) % 360

    def get_direction(self, bearing):
        directions = ["North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"]
        return directions[round(bearing / 45) % 8]

    def get_distance_data(self, country_a: str, country_b: str):
        loc_a = self.geolocator.geocode(country_a)
        loc_b = self.geolocator.geocode(country_b)

        if not loc_a or not loc_b:
            return None

        dist_km = geodesic((loc_a.latitude, loc_a.longitude), (loc_b.latitude, loc_b.longitude)).km
        bearing = self.calculate_bearing(loc_a.latitude, loc_a.longitude, loc_b.latitude, loc_b.longitude)

        return {
            "origin": loc_a.address,
            "destination": loc_b.address,
            "distance_km": round(dist_km, 2),
            "direction": self.get_direction(bearing),
            "bearing_degrees": round(bearing, 2)
        }


geo_service = GeoService()
