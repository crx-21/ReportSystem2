# Model data for my API validates the JSON
# pyrefly: ignore [missing-import]
from fastapi import FastAPI

# pyrefly: ignore [missing-import]
from pydantic import BaseModel


class UserModel(BaseModel):
    email: str
    username: str
    password: str
