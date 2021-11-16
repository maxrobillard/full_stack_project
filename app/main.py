from fastapi import FastAPI, Request, APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.db import crud, schemas
from app.db.models import models
from app.db.database import SessionLocal, engine

from typing import List
from sqlalchemy.orm import Session

models.BaseSQL.metadata.create_all(bind=engine)

app = FastAPI(title="test")

api_router = APIRouter()

app.mount("/static", StaticFiles(directory="./app/static"), name="static")
templates = Jinja2Templates(directory="./app/templates")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@api_router.get("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db, user)


@api_router.get("/", response_class=HTMLResponse, status_code=200)
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


@app.get("/services/app_web")
def read_service1():
    return {"status_code": 200, "message": "service1 is called"}


app.include_router(api_router)