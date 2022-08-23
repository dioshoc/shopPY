from fastapi import FastAPI

from src.db.database import engine
from src.models import models
from src.endpoints import products, category

models.Base.metadata.create_all(bind=engine)

app: FastAPI = FastAPI(title="Store")

app.include_router(products.router)
app.include_router(category.router)
