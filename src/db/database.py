from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.config import Config

config = Config(".env")

DATABASE_URL = config("DATABASE_URL", cast=str, default="")

engine = create_engine(
    DATABASE_URL
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
