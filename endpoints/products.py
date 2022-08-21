from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from crud import productCrud
from endpoints.depends import get_db
from schemas import productsScheme

router = APIRouter()


@router.post("/")
def create_product(product: productsScheme.ProductCreate, db: Session = Depends(get_db)):
    categoryLength = len(product.category)
    if 2 > categoryLength or categoryLength > 10:
        raise HTTPException(status_code=403, detail="Wrong number of categories")
    return productCrud.create_product(db, product=product)


@router.post("/{product_id}/update")
def update_product(product_id: int, product: productsScheme.ProductUpdate, db: Session = Depends(get_db)):
    categoryLength = len(product.category)
    if 2 > categoryLength or categoryLength > 10:
        raise HTTPException(status_code=403, detail="Wrong number of categories")
    return productCrud.update_product(db, product=product, product_id=product_id)


@router.delete("/{product_id}/remove")
def remove_product(product_id: int, db: Session = Depends(get_db)):
    return productCrud.remove_product(db, product_id=product_id)


@router.get("/list")
def read_products(
        skip: int = 0,
        limit: int = 10,
        q: str = '',
        db: Session = Depends(get_db)
):
    return productCrud.get_products(
        db,
        skip=skip,
        limit=limit,
        q=q
    )
