import requests
from fastapi import Request
import traceback
from . import torrent_handler_router
from message_broker import MessageBroker
from core.config import settings


@torrent_handler_router.post('/new_torrent')
async def post_torrent(new_torent: Request):
    new_torrent_data = await new_torent.json()
    try :
        MessageBroker().publish_new_torrent(new_torrent_data)
        return {
            "status": "SUCCESS",
            "data": new_torrent_data
        }
    except Exception:
        return {
            "status" : "Failed",
            "errors" : traceback.format_exc()
        }

@torrent_handler_router.get("/scrap_by_name/{name}")
async def scrap_by_name(name: str, site="yts", limit=20):
    return requests.request("GET", settings.TORRENT_SCRAPPER_URL+f"/api/v1/search?site={site}&query={name}&limit={limit}").json()
