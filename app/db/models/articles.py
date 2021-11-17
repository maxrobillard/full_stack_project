from sqlalchemy import Boolean, Column, ForeignKey, String, Integer, Date
from sqlalchemy.orm import relationship
from app.db.database import Base


class Article(Base):
    __tablename__ = "Article"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String, index=True)
    date_posted = Column(Date, index=True)
    writer_id = Column(Integer, ForeignKey("User.id"))

    writer = relationship("User", back_populates="article")
