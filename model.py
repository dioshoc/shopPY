from sqlalchemy import ForeignKey, Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from db.database import Base


class AssociationTable(Base):
    __tablename__ = "association"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(ForeignKey("products.id"))
    category_id = Column(ForeignKey("category.id"))


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    cost = Column(String)
    published = Column(String)
    deleted = Column(Boolean)

    category = relationship(
        "Category", secondary="association", back_populates="products"
    )


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)

    products = relationship(
        "Product", secondary="association", back_populates="category"
    )
