from sqlalchemy import Boolean, Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from database import BaseSQL


class User(BaseSQL):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    article = relationship("Item", back_populates="writer")


class Article(BaseSQL):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    writer_id = Column(Integer, ForeignKey("users.id"))

    writer = relationship("User", back_populates="article")
