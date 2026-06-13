# pyrefly: ignore [missing-import]
from fastapi import FastAPI, HTTPException
from .schemas import UserModel
from .model import User
from .database import Session

app = FastAPI()


@app.post("/register")
async def Register(db: Session, UserData: UserModel):
    existing_user = db.query(User).filter(User.email == UserData.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    new_user = User(
        email=UserData.email,
        username=UserData.username,
        password=UserData.password,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}
