from typing import List
from pydantic import BaseModel


class ArticleBase(BaseModel):
    title: str
    body: str = None


class ArticleCreate(BaseModel):
    pass


class Article(ArticleBase):
    id: int
    writer_id: int

    class Config:
        orm_mode = True
