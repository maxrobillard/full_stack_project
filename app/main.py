from fastapi import FastAPI
from app.apis.base import api_router
from fastapi.staticfiles import StaticFiles

from app.db.database import SessionLocal, engine
from app.db.base import BaseSQL


def configure_static(app):
    app.mount("/static", StaticFiles(directory="./app/static"), name="static")


def include_router(app):
    app.include_router(api_router)


def create_tables():
    print("create_tables")
    BaseSQL.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI(title="test")
    include_router(app)
    configure_static(app)
    create_tables()
    return app


app = start_application()
