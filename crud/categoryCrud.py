from sqlalchemy import delete
from sqlalchemy.orm import Session

import model
from schemas import categoryScheme


def get_category(db: Session, category_id: int):
    return db.query(model.AssociationTable).filter(model.AssociationTable.category_id == category_id).all()


def get_category_list(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: categoryScheme.CategoryCreate):
    db_category = model.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category


def remove_category(db: Session, category_id: int):
    db.execute(
        delete(model.Category).
        where(model.Category.id == category_id)
    )
    db.commit()
    return []
