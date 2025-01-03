from fastapi import APIRouter
from app.api.models import OrderIn, OrderOut
import httpx
from fastapi import HTTPException
from typing import List
from app.api import db_manager
from app.api.services import is_user_present, is_product_present

orders_router = APIRouter()

@orders_router.get("/home")
def root():
    return {"message": "Order Service"}

@orders_router.post("/", status_code=201)
async def create_order(order: OrderIn):
    #check user exists
    if not is_user_present(order.user_id):
        raise HTTPException(status_code=404, detail=f"User not found for id: {order.user_id}")
    
    #check product exists
    if not is_product_present(order.product_id):
        raise HTTPException(status_code=404, detail=f"Product not found for id: {order.product_id}")
    
    order_id = await db_manager.add_order(order)
    response = {
        'id': order_id,
        **order.dict()
    }

    return response

@orders_router.get("/", response_model=List[OrderOut])
async def get_all_orders():
   return await db_manager.get_all_orders()

@orders_router.get("/{id}/")
async def get_order(id: int):
    order = await db_manager.get_order(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    return order

@orders_router.get("/user/{user_id}/")
async def get_orders_by_user(user_id: int):
    #check user exists
    if not is_user_present(user_id):
        raise HTTPException(status_code=404, detail=f"User not found for id: {user_id}")
    order = await db_manager.get_order_by_user(user_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order not found for user id: {user_id}")
    return order