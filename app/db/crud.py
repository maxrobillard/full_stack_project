import hashlib

from sqlalchemy.orm import Session

from app.db.models.users import User
from app.db.models.articles import Article
from app.db.schemas.article import ArticleCreate
from app.db.schemas.user import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 50):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    hashed_password = hashlib.sha1(user.password).hexdigest()
    db_user = User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_user_article(db: Session, article: ArticleCreate, user_id: int):
    db_article = Article(**article.dict(), writer_id=user_id)
    db.add(db_article)
    db.commit()
    db.refresh(db_article)
    return db_article


def get_articles(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Article).offset(skip).limit(limit).all()
