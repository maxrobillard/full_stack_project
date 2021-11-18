from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status

from app.db.database import get_db
from app.schemas.article import ArticleCreate, ShowArticle
from app.db.repository.articles import create_new_article, retreive_article, list_articles, update_article_by_id, delete_article_by_id
from app.apis.version1.route_login import get_current_user_from_token
from typing import List
from app.db.models.users import User

router = APIRouter()


@router.post("/create-article/", response_model=ShowArticle)
def create_article(article: ArticleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    article = create_new_article(article=article, db=db, writer_id=current_user.id)
    return article


@router.get("/get/{id}", response_model=ShowArticle)
def read_article(id: int, db: Session = Depends(get_db)):
    article = retreive_article(id=id, db=db)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"L'article avec cette id {id} n'existe pas")
    return article


@router.get("/all", response_model=List[ShowArticle])
def read_articles(db: Session = Depends(get_db)):
    articles = list_articles(db=db)
    return articles


@router.put("/update/{id}")
def update_article(id: int, article: ArticleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    message = update_article_by_id(id=id, article=article, db=db, writer_id=current_user.id)
    if not message:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"L'article avec l'id {id} n'a pas été trouvé")
    return {"msg":"Les données ont été mise à jour"}


@router.delete("/delete/{id}")
def delete_article(id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user_from_token)):
    article = retreive_article(id=id, db=db)
    print(article.id)
    if not article:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"L'article avec l'id {id} n'a pas été trouvé")
    print(article.writer_id, current_user.id, current_user.is_superuser)
    if article.writer_id == current_user.id or current_user.is_superuser:
        delete_article_by_id(id=id, db=db, writer_id=current_user.id)
        print("Supprimé avec succés")
        return {"detail": "Supprimé avec succés"}
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Vous n'êtes pas autorisé à faire cela !"
    )
