from fastapi.responses import RedirectResponse
from fastapi.security.utils import get_authorization_scheme_param

from app.apis.version1.route_login import login_for_access_token
from app.db.database import get_db
from fastapi import APIRouter, Depends, Request, Response, status, HTTPException
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.apis.version1.route_login import get_current_user_from_token, logout_token, get_current_token
from app.webapps.auth.forms import LoginForm
from fastapi.responses import HTMLResponse
from app.db.models.users import User


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


@api_router.get("/logout")
def logout_remove_cookie(request: Request, response: Response, user: User = Depends(get_current_user_from_token)):
    if user.is_active:
        response = templates.TemplateResponse("homepage.html", {"request": request})
        logout_token(response=response)

    return response


async def connected(current_user: User = Depends(get_current_user_from_token)):
    print(current_user.is_active)
    print(current_user.username)
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Utilisateur non connecté")
    return {"connecte": current_user.username}


@api_router.get("/profil")
def profil(request: Request, db: Session = Depends(get_db)):

    authorization: str = request.cookies.get("access_token")

    if authorization is not None:
        scheme, param = get_authorization_scheme_param(authorization)
        user = get_current_user_from_token(param, db)
        return templates.TemplateResponse("profil.html", {"request": request, "user": user})
    return RedirectResponse("/connexion")






