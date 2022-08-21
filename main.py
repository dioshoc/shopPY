from fastapi import FastAPI

from db.database import engine
from endpoints import products, category
import model

model.Base.metadata.create_all(bind=engine)

app: FastAPI = FastAPI(title="Store")

app.include_router(products.router, prefix="/product", tags=["product"])
app.include_router(category.router, prefix="/category", tags=["category"])

