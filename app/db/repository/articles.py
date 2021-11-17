from sqlalchemy.orm import Session

from app.schemas.article import ArticleCreate
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


def list_articles(db: Session):
    articles = db.query(Article).all()
    return articles


def update_article_by_id(id: int, article: ArticleCreate, db: Session, writer_id):
    existing_article = db.query(Article).filter(Article.id == id)
    if not existing_article.first():
        return 0
    article.__dict__.update(writer_id=writer_id)
    existing_article.update(article.__dict__)
    db.commit()
    return 1


def delete_article_by_id(id: int, db: Session, writer_id):
    existing_article = db.query(Article).filter(Article.id == id)
    if not existing_article.first():
        return 0
    existing_article.delete(synchronize_session=False)
    db.commit()
    return 1


def search_article(query: str, db: Session):
    print("la requete est :" + query)
    articles = db.query(Article).filter(Article.title.contains(query))
    return articles
