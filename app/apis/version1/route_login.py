from fastapi.security import OAuth2PasswordRequestForm
from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import status,HTTPException

from app.db.database import get_db
from app.core.hashing import Hasher
from app.schemas.tokens import Token
from app.db.repository.login import get_user
from app.core.security import create_access_token
from app.core.config import settings


router = APIRouter()


def authenticate_user(email: str, password: str, db: Session):
    user = get_user(email= email, db=db)
    print(user)
    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user


@router.post("/token", response_model=Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.email, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Email ou mot de passe incorrect",
        )
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}