from fastapi.security import OAuth2PasswordRequestForm
from app.apis.utils import OAuth2PasswordBearerWithCookie
from fastapi import Depends, APIRouter, Response
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from datetime import timedelta
from fastapi import status, HTTPException

from app.db.database import get_db
from app.core.hashing import Hasher
from app.schemas.tokens import Token
from app.db.repository.login import get_user
from app.core.security import create_access_token
from app.core.config import settings


router = APIRouter()


def authenticate_user(email: str, password: str, db: Session):
    user = get_user(email=email, db=db)
    print(user)

    if not user:
        return False
    if not Hasher.verify_password(password, user.hashed_password):
        return False
    return user


@router.post("/token", response_model=Token)
def login_for_access_token(response: Response, form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Email ou mot de passe incorrect")
    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub": user.email}, expires_delta=access_token_expires)
    response.set_cookie(key="access_token", value=f"Bearer {access_token}", httponly=True)
    return {"access_token": access_token, "token_type": "bearer"}


oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl='/login/token')


@router.post("/token", response_model=Token)
def logout_token(response: Response):
    response.delete_cookie(key="access_token")
    access_token = None
    return {"access_token": access_token, "token_type": "bearer"}


def get_current_user_from_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Impossible de valider les identifiants")
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        email: str = payload.get("sub")
        print("l'email extraite est", email)
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(email=email, db=db)
    if user is None:
        raise credentials_exception
    return user


def get_current_token(token: str = Depends(oauth2_scheme)):
    print(token)
    return token
