from fastapi import FastAPI, Request, APIRouter, Depends, HTTPException
from fastapi import Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="./app/templates")
api_router = APIRouter()


@api_router.get("/inscription", response_class=HTMLResponse, status_code=200)
async def read_index(request: Request):
    return templates.TemplateResponse("inscription.html", {"request": request})


@api_router.get("/connexion", response_class=HTMLResponse, status_code=200)
async def read_index(request: Request):
    return templates.TemplateResponse("connexion.html", {"request": request})


@api_router.get("/aide", response_class=HTMLResponse, status_code=200)
async def read_index(request: Request):
    return templates.TemplateResponse("aide.html", {"request": request})


@api_router.get("/services/app_web")
def read_service1():
    return {"status_code": 200, "message": "service1 is called"}