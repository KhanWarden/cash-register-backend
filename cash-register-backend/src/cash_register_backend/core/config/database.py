from pydantic import BaseModel


class DatabaseConfig(BaseModel):
    url: str
    echo: bool = False
    timeout: int = 30
