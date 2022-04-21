from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    PROJECT_NAME:str = "Torrent Board"
    PROJECT_VERSION: str = "1.0.0"
    RABBITMQ_URL: str = "rabbitmq"
    TORRENT_SCRAPPER_URL : str = "https://torrents-api-py3.herokuapp.com"
    TMDB_URL : str = "https://api.themoviedb.org"
    TMDB_KEY: str
    
    class Config:
        env_file = ".env"

@lru_cache
def get_settings():
    return Settings()
    
settings = get_settings()