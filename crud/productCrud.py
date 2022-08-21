from sqlalchemy import update, delete
from sqlalchemy.orm import Session

import model
from schemas import productsScheme


def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model.Product).offset(skip).limit(limit).all()


def create_product(db: Session, product: productsScheme.ProductCreate):
    categories = db.query(model.Category).filter(model.Category.id.in_(product.category)).all()

    product_dict = product.dict()
    product_dict.pop('category')

    db_product = model.Product(**product_dict, deleted=False)

    db_product.category.extend(categories)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def remove_product(db: Session, product_id: int):
    db.execute(
        update(model.Product).
        where(model.Product.id == product_id).
        values(deleted=True)
    )
    db.execute(
        delete(model.AssociationTable).
        where(model.AssociationTable.product_id == product_id)
    )
    db.commit()
    return []


def update_product(
        db: Session,
        product: object,
        product_id: int
):
    db.execute(
        update(model.Product).
        where(model.Product.id == product_id).
        values(**product.dict())
    )
    db.commit()
    return model.Product
