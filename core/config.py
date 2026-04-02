from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    # API Metadata
    PROJECT_NAME: str = "Map Guesser"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    # Geo Service Settings
    GEO_USER_AGENT: str = "my_distance_calculator_v1"
    GEO_TIMEOUT: int = 10

    # Security (Placeholder for your future Auth)
    SECRET_KEY: str = "your-super-secret-key-here"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8  # 8 days

    # Tells Pydantic to read from a .env file if it exists
    model_config = SettingsConfigDict(env_file=".env")

# Global instance to be imported elsewhere
settings = Settings()
