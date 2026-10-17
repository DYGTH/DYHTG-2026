from fastapi import FastAPI

from app.routes import router

app = FastAPI(title="Resources game", version="0.0.0")

app.include_router(router)
