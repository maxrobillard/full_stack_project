from sqlalchemy import Boolean, Column, ForeignKey, String, Integer
from sqlalchemy.orm import relationship

from app.db.database import BaseSQL


class User(BaseSQL):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean, default=True)
    is_superuser = Column(Boolean(), default=False)
    article = relationship("Article", back_populates="writer")
    