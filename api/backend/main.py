from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.config import settings
from functools import lru_cache
from apis.general_pages.route_homepage import general_pages_router
from apis.torrent_handler import torrent_handler_router

origins = ["*"]



def include_router(app):
    app.include_router(general_pages_router)
    app.include_router(torrent_handler_router)


def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    app.add_middleware(
        CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"]
    )
    include_router(app)
    return app

app = start_application()
