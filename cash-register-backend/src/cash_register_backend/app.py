from fastapi import FastAPI

from cash_register_backend.core.config import settings

app = FastAPI(
    title=settings.app.title,
)
