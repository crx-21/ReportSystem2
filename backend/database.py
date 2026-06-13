# This file knows how to talk to the database

# pyrefly: ignore [missing-import]
from sqlalchemy import create_engine

# pyrefly: ignore [missing-import]
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "reportdb"


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)
Base = declarative_base()
