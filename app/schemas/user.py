from typing import List
from pydantic import BaseModel, EmailStr
from app.schemas.article import Article


class UserBase(BaseModel):
    email: EmailStr


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    articles: List[Article] = []

    class Config:
        orm_mode = True


class ShowUser(BaseModel):
    username: str
    email: EmailStr
    is_active: bool

    class Config():
        orm_mode = True
