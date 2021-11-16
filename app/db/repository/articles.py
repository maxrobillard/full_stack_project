from sqlalchemy.orm import Session

from app.db.schemas.article import ArticleCreate
from app.db.models.articles import Article


def create_new_article(article: ArticleCreate, db: Session, writer_id: int):
    article_object = Article(**article.dict(), writer_id=writer_id)
    db.add(article_object)
    db.commit()
    db.refresh(article_object)
    return article_object


def retreive_article(id: int, db: Session):
    item = db.query(Article).filter(Article.id == id).first()
    return item
