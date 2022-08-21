from typing import Union, List

from pydantic import BaseModel


class ProductBase(BaseModel):
    name: str
    description: Union[str, None] = None
    cost: int
    published: bool
    category: List[int]

    class Config:
        orm_mode = True


class ProductCreate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    category: List[int]

    class Config:
        ignore_extras = True


class ProductUpdate(ProductBase):
    pass


class ProductRemove(BaseModel):
    id: int
    deleted: bool


class Product(ProductBase):
    id: int
    deleted: bool

    class Config:
        orm_mode = True
