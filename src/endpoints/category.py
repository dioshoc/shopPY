from fastapi import Depends, HTTPException, APIRouter
from sqlalchemy.orm import Session

from src.crud import category_crud
from src.endpoints.depends import get_db
from src.models.models import Category
from src.schemas.category_scheme import CategoryCreate

router = APIRouter(prefix="/category", tags=["category"])


@router.post("", response_model=Category)
def create_category(
        category: CategoryCreate,
        db: Session = Depends(get_db)
):
    return category_crud.create_category(db=db, category=category)


@router.get("")
def get_category_list(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return category_crud.get_category_list(db, skip=skip, limit=limit)


@router.delete("/{category_id}")
def remove_category(category_id: int, db: Session = Depends(get_db)):
    db_category = category_crud.get_category(db, category_id=category_id)

    if db_category:
        raise HTTPException(status_code=403, detail="Category has product")

    category_crud.remove_category(db, category_id=category_id)
    return db_category
