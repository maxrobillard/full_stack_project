from fastapi import APIRouter, responses, status
from fastapi import Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from app.webapps.articles.forms import ArticleCreateForm
from app.db.repository.articles import list_articles, retreive_article
from app.schemas.article import ArticleCreate
from fastapi.security.utils import get_authorization_scheme_param
from app.apis.version1.route_login import get_current_user_from_token
from app.db.database import get_db
from app.db.models.users import User
from app.db.repository.articles import create_new_article, search_article
from typing import Optional

templates = Jinja2Templates(directory="./app/templates")
router = APIRouter(include_in_schema=False)


@router.get("/")
async def home(request: Request, db: Session = Depends(get_db), msg: str = None):
    articles = list_articles(db=db)
    return templates.TemplateResponse("homepage.html", {"request": request, "articles": articles, "msg": msg})


@router.get('/details/{id}')
def article_detail(id: int, request: Request, db: Session = Depends(get_db)):
    article = retreive_article(id=id, db=db)
    return templates.TemplateResponse("detail.html", {"request": request, "article": article})


@router.get("/post_article")
def create_article(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("create_article.html", {'request': request})


@router.post("/post_article")
async def create_article(request: Request, db: Session = Depends(get_db)):
    form = ArticleCreateForm(request)
    await form.load_data()
    if form.is_valid():
        try:
            token = request.cookies.get("access_token")
            scheme, param = get_authorization_scheme_param(token)
            current_user: User = get_current_user_from_token(token=param, db=db)
            article = ArticleCreate(**form.__dict__)
            article = create_new_article(article=article, db=db, writer_id=current_user.id)
            return responses.RedirectResponse(
                f"/details/{article.id}", status_code=status.HTTP_302_FOUND
            )
        except Exception as e:
            print(e)
            form.__dict__.get("errors").append("Vous devez être connecté pour cela")
            return templates.TemplateResponse("connexion.html", form.__dict__)

    return templates.TemplateResponse("create_article.html", form.__dict__)


@router.get("/delete_article")
def show_articles_to_delete(request: Request, db: Session = Depends(get_db)):
    articles = list_articles(db=db)
    return templates.TemplateResponse("delete_articles.html", {"request": request, "articles": articles})


@router.get("/search")
def search(request: Request, db: Session = Depends(get_db), query: Optional[str] = None):
    articles = search_article(query, db=db)
    return templates.TemplateResponse("homepage.html", {"request": request, "articles": articles})