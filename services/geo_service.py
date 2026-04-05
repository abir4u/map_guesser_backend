import math
import io
import pycountry
import geopandas as gpd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from core.config import settings


class GeoService:
    def __init__(self):
        self.geolocator = Nominatim(
            user_agent=settings.GEO_USER_AGENT,
            timeout=settings.GEO_TIMEOUT
        )
        # Load dataset
        self.world = gpd.read_file("data/countries/ne_110m_admin_0_countries.shp")

    def get_all_countries(self):
        return sorted([c.name for c in pycountry.countries])

    def get_distance_data(self, country_a: str, country_b: str):
        loc_a = self.geolocator.geocode(country_a)
        loc_b = self.geolocator.geocode(country_b)

        if not loc_a or not loc_b:
            return None

        # Logic for distance and bearing
        coords_a = (loc_a.latitude, loc_a.longitude)
        coords_b = (loc_b.latitude, loc_b.longitude)

        dist_km = geodesic(coords_a, coords_b).km
        bearing = self._calculate_bearing(loc_a.latitude, loc_a.longitude, loc_b.latitude, loc_b.longitude)

        return {
            "origin": loc_a.address,
            "destination": loc_b.address,
            "distance_km": round(dist_km, 2),
            "direction": self._get_direction(bearing),
            "bearing_degrees": round(bearing, 2)
        }

    def get_country_outline(self, country_name: str):
        country_name = handle_exception_data_for_outline(country_name)
        country_data = self.world[
            self.world['ADMIN'].str.lower() == country_name.lower()
            ]
        if country_data.empty:
            return None

        fig, ax = plt.subplots(figsize=(5, 5))
        country_data.plot(ax=ax, color='white', edgecolor='black', linewidth=2)
        ax.set_axis_off()

        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)
        buf.seek(0)
        plt.close(fig)
        return buf

    def _calculate_bearing(self, lat1, lon1, lat2, lon2):
        lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
        d_lon = lon2 - lon1
        y = math.sin(d_lon) * math.cos(lat2)
        x = math.cos(lat1) * math.sin(lat2) - math.sin(lat1) * math.cos(lat2) * math.cos(d_lon)
        return (math.degrees(math.atan2(y, x)) + 360) % 360

    def _get_direction(self, bearing):
        directions = ["North", "North-East", "East", "South-East", "South", "South-West", "West", "North-West"]
        return directions[round(bearing / 45) % 8]


geo_service = None

def get_geo_service():
    global geo_service
    if geo_service is None:
        geo_service = GeoService()
    return geo_service

def handle_exception_data_for_outline(country_name: str):
    name = country_name
    match name:
        case "United States":
            country_name = "United States of America"
        case "Venezuela, Bolivarian Republic of":
            country_name = "Venezuela"
        case "Bahamas":
            country_name = "The Bahamas"
        case "Brunei Darussalam":
            country_name = "Brunei"
        case "Congo":
            country_name = "Democratic Republic of the Congo"
        case "American Samoa":
            country_name = "NEED TO FIND OUT"
        case "Palau":
            country_name = "NEED TO FIND OUT"
        case "Bahrain":
            country_name = "NEED TO FIND OUT"
        case "Sint Maarten (Dutch part)":
            country_name = "NEED TO FIND OUT"

    return country_name
