from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # API Metadata
    PROJECT_NAME: str = "Map Guesser"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Geo Service Settings
    GEO_USER_AGENT: str = "my_distance_calculator_v1"
    GEO_TIMEOUT: int = 10

    # Tells Pydantic to read from a .env file if it exists
    model_config = SettingsConfigDict(env_file=".env")

    MONGO_URI: str = "mongodb://localhost:27017"
    DATABASE_NAME: str = "map_guesser"

# Global instance to be imported elsewhere
settings = Settings()
