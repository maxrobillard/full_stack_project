from sqlalchemy import Boolean, Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from app.db.database import BaseSQL


class Article(BaseSQL):
    __tablename__ = 'article'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    writer_id = Column(Integer, ForeignKey("users.id"))

    writer = relationship("User", back_populates="article")
