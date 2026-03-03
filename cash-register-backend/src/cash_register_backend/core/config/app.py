from pydantic import BaseModel


class AppConfig(BaseModel):
    title: str = "Cash Register Backend"
    host: str = "0.0.0.0"
    port: str = "8000"
