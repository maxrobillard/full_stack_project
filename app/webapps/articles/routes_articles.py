from fastapi import APIRouter
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.db.repository.articles import list_articles, retreive_article
from app.db.database import get_db


templates = Jinja2Templates(directory="./app/templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db)):
    articles = list_articles(db=db)
    return templates.TemplateResponse("homepage.html", {"request": request,"articles":articles})


@router.get('/details/{id}')
def article_detail(id: int, request: Request, db: Session = Depends(get_db)):
    article = retreive_article(id=id, db=db)
    return templates.TemplateResponse("detail.html", {"request": request, "article": article})
