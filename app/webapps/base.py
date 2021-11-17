from app.webapps.articles import routes_articles
from fastapi import APIRouter


api_router = APIRouter()
api_router.include_router(routes_articles.router, prefix="", tags=["article_webapp"])
