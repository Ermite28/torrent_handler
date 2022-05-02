import requests
from fastapi import Depends, Request
import traceback
from . import torrent_handler_router
from message_broker import MessageBroker
from core.config import Settings
from functools import lru_cache

@lru_cache
def get_settings():
    return Settings()


@torrent_handler_router.post("/new_torrent")
async def post_torrent(new_torent: Request):
    new_torrent_data = await new_torent.json()
    try:
        MessageBroker().publish_new_torrent(new_torrent_data)
        return {"status": "SUCCESS", "data": new_torrent_data}
    except Exception:
        return {"status": "Failed", "errors": traceback.format_exc()}


@torrent_handler_router.get("/scrap_by_name/{name}")
async def scrap_by_name(name: str, site="yts", limit=20, settings: Settings = Depends(get_settings)):
    try:
        movies = requests.request(
            "GET", settings.TORRENT_SCRAPPER_URL + f"/api/v1/search?site={site}&query={name}&limit={limit}"
        ).json()['data'][0]
    except:
        movies = {'torrents': [{"quality": "unavailable", "score": 0}]}
    return movies


@torrent_handler_router.get("/search_movies_by_name/{name}")
async def search_movies_by_name(name: str, language="fr-EU", settings: Settings = Depends(get_settings)):
    return requests.request(
        "GET", settings.TMDB_URL + f"/3/search/movie?api_key={settings.TMDB_KEY}&language={language}&query={name}"
    ).json()
