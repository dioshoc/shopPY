from sqlalchemy import delete
from sqlalchemy.orm import Session

from src.models.models import AssociationTable, Category
from src.schemas.category_scheme import CategoryCreate


def get_category(db: Session, category_id: int):
    return db.query(AssociationTable).filter(AssociationTable.category_id == category_id).all()


def get_category_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: CategoryCreate):
    db_category = Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def remove_category(db: Session, category_id: int):
    db.execute(
        delete(Category).
        where(Category.id == category_id)
    )
    db.commit()
    return []
