from fastapi import APIRouter

from app.apis.version1 import routes
from app.apis.version1 import route_users
from app.apis.version1 import route_articles


api_router = APIRouter()
api_router.include_router(routes.api_router, prefix="", tags=["general_pages"])
api_router.include_router(route_users.router, prefix="/users", tags=["users"])
api_router.include_router(route_articles.router, prefix="/articles", tags=["articles"])
