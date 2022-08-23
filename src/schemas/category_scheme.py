from typing import List

from pydantic import BaseModel


class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryRemove(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    products: List[int]

    class Config:
        orm_mode = True


class CategoryResponse(CategoryBase):
    id: int
