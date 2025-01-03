from fastapi import APIRouter
from fastapi import HTTPException
from app.api.models import ProductOut, ProductIn
from typing import List
from app.api import db_manager

products_router = APIRouter()

@products_router.get("/home/")
def root():
    return {"message": "Product Service"}

@products_router.post("/", status_code=201)
async def create_product(product: ProductIn):
    product_id = await db_manager.add_product(product)
    response = {
        'id': product_id,
        **product.dict()
    }

    return response

@products_router.get("/", response_model=List[ProductOut])
async def get_all_products():
   return await db_manager.get_all_products()

@products_router.get("/{id}/")
async def get_product(id: int):
    product = await db_manager.get_product(id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product