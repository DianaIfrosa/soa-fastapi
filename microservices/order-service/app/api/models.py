from pydantic import BaseModel

class OrderIn(BaseModel):
    user_id: int
    product_id: int
    date: str
    address: str

class OrderOut(OrderIn):
    id: int 