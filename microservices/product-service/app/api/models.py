from pydantic import BaseModel

class ProductIn(BaseModel):
    name: str
    price: float

class ProductOut(ProductIn):
    id: int