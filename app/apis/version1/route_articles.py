from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from app.db.database import get_db
from app.db.models.articles import Article
from app.db.schemas.article import ArticleCreate, ShowArticle
from app.db.repository.articles import create_new_article, retreive_article

router = APIRouter()


@router.post("/create-article/", response_model=ShowArticle)
def create_article(article: ArticleCreate, db: Session = Depends(get_db)):
    current_user = 1
    article = create_new_article(article=article, db=db, writer_id=current_user)
    return article


@router.get("/get/{id}", response_model=ShowArticle)
def read_article(id: int, db: Session = Depends(get_db)):
    article = retreive_article(id=id, db=db)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"L'article avec cette id {id} n'existe pas")
    return article
