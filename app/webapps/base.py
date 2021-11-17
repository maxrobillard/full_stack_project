from app.webapps.articles import routes_articles
from app.webapps.users import routes_users
from app.webapps.auth import routes_login
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(routes_articles.router, prefix="", tags=["article_webapp"])
api_router.include_router(routes_users.api_router, prefix="", tags=['user_webapp'])
api_router.include_router(routes_login.api_router, prefix="", tags=['login_webapp'])
