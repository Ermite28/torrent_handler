from . import torrent_handler_router
from fastapi import Request
from message_broker import MessageBroker
import traceback


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