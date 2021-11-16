from typing import Optional
from pydantic import BaseModel
from datetime import date, datetime


class ArticleBase(BaseModel):
    title: str
    body: str = None
    date_posted: Optional[date] = datetime.now().date()


class ArticleCreate(BaseModel):
    pass


class Article(ArticleBase):
    id: int
    writer_id: int

    class Config:
        orm_mode = True


class ShowArticle(ArticleBase):
    title: str
    body: str
    date_posted: date

    class Config():
        orm_mode = True
