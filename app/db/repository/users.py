from sqlalchemy.orm import Session

from app.schemas.user import UserCreate
from app.db.models.users import User
from app.core.hashing import Hasher


def create_new_user(user: UserCreate, db: Session):
    user = User(username=user.username,
                email=user.email,
                hashed_password=Hasher.get_password_hash(user.password),
                is_active=True,
                is_superuser=False
                )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


def get_user_by_email(email: str, db: Session):
    user = db.query(User).filter(User.email == email).first()
    return user


def get_user_by_id(id: int, db: Session):
    user = db.query(User).filter(User.id == id).first()
    return user


def get_all_user(db: Session):
    users = db.query(User).all()
    return users