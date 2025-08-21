from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "CLI - File Generator"
    ENV: str = "development"
    VERSION: str = "1.0"
    DEBUG: bool = True
    LOGFIRE_TOKEN: str | None = None
    
    class Config:
        env_file = ".env"

settings = Settings()