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


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    articles: List[Article] = []

    class Config:
        orm_mode = True
