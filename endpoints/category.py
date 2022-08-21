from typing import List

from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from crud import categoryCrud
from endpoints.depends import get_db
from schemas import categoryScheme

router = APIRouter()


@router.post("/", response_model=categoryScheme.Category)
def create_category(
        category: categoryScheme.CategoryCreate,
        db: Session = Depends(get_db)
):
    return categoryCrud.create_category(db=db, category=category)


@router.get("/list")
def get_category_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return categoryCrud.get_category_list(db, skip=skip, limit=limit)


@router.delete("/{category_id}/remove")
def remove_category(category_id: int, db: Session = Depends(get_db)):
    db_category = categoryCrud.get_category(db, category_id=category_id)

    if db_category:
        raise HTTPException(status_code=403, detail="Category has product")

    categoryCrud.remove_category(db, category_id=category_id)
    return db_category
