from pydantic import BaseModel


class Association(BaseModel):
    id: int
    product_id: int
    category: int