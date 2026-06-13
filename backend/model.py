# This file writes SQL for the database

# pyrefly: ignore [missing-import]
from sqlalchemy import Column, Integer, String, Boolean, DateTime
from .database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "reportdb"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
