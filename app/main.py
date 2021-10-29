from fastapi import FastAPI, Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(title="test")

api_router = APIRouter()

app.mount("/static", StaticFiles(directory="./app/static"), name="static")
templates = Jinja2Templates(directory="./app/templates")


@api_router.get("/" , response_class=HTMLResponse, status_code=200)
async def read_root(request: Request):
    return templates.TemplateResponse("inscription.html", {"request": request})


@api_router.get("/items/{items_id}", response_class=HTMLResponse)
async def read_item(request: Request, items_id: str):
    return templates.TemplateResponse("item.html", {"request": request, "items_id": items_id})


@api_router.get("/inscription", response_class=HTMLResponse, status_code=200)
async def read_index(request: Request):
    return templates.TemplateResponse("inscription.html", {"request": request})


@api_router.get("/connexion", response_class=HTMLResponse, status_code=200)
async def read_index(request: Request):
    return templates.TemplateResponse("connexion.html", {"request": request})


@api_router.get("/aide", response_class=HTMLResponse, status_code=200)
async def read_index(request: Request):
    return templates.TemplateResponse("aide.html", {"request": request})


app.include_router(api_router)