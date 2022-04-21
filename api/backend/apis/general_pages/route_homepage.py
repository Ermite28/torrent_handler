from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

general_pages_router = APIRouter()

@general_pages_router.get('/')
async def home(request: Request):
    return {"msg": "hello"}