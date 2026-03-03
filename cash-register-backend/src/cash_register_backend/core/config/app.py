from pydantic import BaseModel


class AppConfig(BaseModel):
    title: str = "Cash Register Backend"
    host: str = "0.0.0.0"
    port: int = 8000
    reload: bool = False
