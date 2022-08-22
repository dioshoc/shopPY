from fastapi import Depends, APIRouter, HTTPException, Query
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
        offset: int = Query(0, alias="pagination[offset]"),
        limit: int = Query(10, alias="pagination[limit]"),
        q: str = Query(None, alias="filter[q]"),
        category_id: int = Query(None, alias="filter[category_id]"),
        category_name: str = Query(None, alias="filter[category_name]"),
        min_price: int = Query(None, alias="filter[min_price]"),
        max_price: int = Query(None, alias="filter[max_price]"),
        public: bool = Query(True, alias="filter[public]"),
        deleted: bool = Query(False, alias="filter[deleted]"),
        db: Session = Depends(get_db)
):
    return productCrud.get_products(
        db,
        offset=offset,
        limit=limit,
        search_string=q,
        category_id=category_id,
        category_name=category_name,
        min_price=min_price,
        max_price=max_price,
        public=public,
        deleted=deleted
    )
