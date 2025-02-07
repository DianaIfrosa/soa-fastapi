from pydantic import BaseModel
from typing import List

class OrderIn(BaseModel):
    user_id: int
    product_ids: List[int]
    date: str
    address: str

class OrderOut(OrderIn):
    id: int 