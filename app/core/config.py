from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class Settings(BaseSettings):
    database_url:str
    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()
