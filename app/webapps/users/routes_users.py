from app.db.repository.users import create_new_user
from app.db.database import get_db
from fastapi import APIRouter, Depends, Request, responses, status
from fastapi.templating import Jinja2Templates
from app.schemas.user import UserCreate
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from app.webapps.users.forms import UserCreateForm
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="./app/templates")
api_router = APIRouter()


@api_router.get("/inscription", response_class=HTMLResponse, status_code=200)
def inscription(request: Request, msg: str = None):
    return templates.TemplateResponse("inscription.html", {"request": request, "msg": msg})


@api_router.post("/inscription")
async def inscription(request: Request, db: Session = Depends(get_db)):
    form = UserCreateForm(request)
    await form.load_data()
    if await form.is_valid():
        user = UserCreate(username=form.username, email=form.email, password=form.password)
        try:
            user = create_new_user(user=user, db=db)
            return responses.RedirectResponse("/?msg= Inscription réussie", status_code=status.HTTP_302_FOUND)
        except IntegrityError:
            form.__dict__.get("errors").append("l'adresse mail est déjà utilisée")
            return templates.TemplateResponse("inscription.html", form.__dict__)
    return templates.TemplateResponse("inscription.html", form.__dict__)


