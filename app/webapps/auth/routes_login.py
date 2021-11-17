from app.apis.version1.route_login import login_for_access_token
from app.db.database import get_db
from fastapi import APIRouter, Depends, Request, responses, status, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.webapps.auth.forms import LoginForm
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="./app/templates")
api_router = APIRouter()


@api_router.get("/connexion", response_class=HTMLResponse, status_code=200)
async def login(request: Request):
    return templates.TemplateResponse("connexion.html", {"request": request})


@api_router.post("/connexion")
async def login(request: Request, db: Session = Depends(get_db)):
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Connexion réussie")
            response = templates.TemplateResponse("connexion.html", form.__dict__)
            login_for_access_token(response=response, form_data=form, db=db)
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Email ou mot de passe incorrect")
            return templates.TemplateResponse("connexion.html", form.__dict__)
    return templates.TemplateResponse("connexion.html", form.__dict__)
