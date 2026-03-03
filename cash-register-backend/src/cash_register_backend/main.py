import uvicorn

from cash_register_backend.app import app
from cash_register_backend.core.config import settings

if __name__ == "__main__":
    uvicorn.run(
        app,
        host=settings.app.host,
        port=settings.app.port,
        reload=settings.app.reload,
    )
