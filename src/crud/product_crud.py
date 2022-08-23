from sqlalchemy import update, delete
from sqlalchemy.orm import Session

from src.models.models import Category, Product, AssociationTable
from src.schemas.products_scheme import ProductCreate


def get_products(
        db: Session,
        offset: int,
        limit: int,
        search_string: str,
        category_id: int,
        category_name: str,
        min_price: int,
        max_price: int,
        public: bool,
        deleted: bool
):

    if category_name:
        category_id = db.query(Category).filter(Category.name.like(f'%{category_name}%')).first().id

    categoryProduct = db.query(Product) \
        .join(AssociationTable) \
        .filter(AssociationTable.category_id == category_id)

    if categoryProduct.all():
        products = categoryProduct
    else:
        products = db.query(Product)

    products \
        .filter(Product.published == public) \
        .filter(Product.deleted == deleted)

    if search_string is not None:
        products = products.filter(Product.name.like(f'%{search_string}%'))
    if min_price is not None:
        products = products.filter(Product.cost >= min_price)
    if max_price is not None:
        products = products.filter(Product.cost <= max_price)

    return products.offset(offset).limit(limit).all()


def create_product(db: Session, product: ProductCreate):
    categories = db.query(Category).filter(Category.id.in_(product.category)).all()

    product_dict = product.dict()
    product_dict.pop('category')

    db_product = Product(**product_dict, deleted=False)

    db_product.category.extend(categories)

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def remove_product(db: Session, product_id: int):
    db.execute(
        update(Product).
        where(Product.id == product_id).
        values(deleted=True)
    )
    db.execute(
        delete(AssociationTable).
        where(AssociationTable.product_id == product_id)
    )
    db.commit()
    return []


def update_product(
        db: Session,
        product: object,
        product_id: int
):
    db.execute(
        update(Product).
        where(Product.id == product_id).
        values(**product.dict())
    )
    db.commit()
    return Product
