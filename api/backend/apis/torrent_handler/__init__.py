from fastapi import APIRouter

torrent_handler_router = APIRouter()

from .routes import *
