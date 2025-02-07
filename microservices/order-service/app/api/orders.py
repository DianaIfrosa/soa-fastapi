from fastapi import APIRouter, Depends
from app.api.models import OrderIn, OrderOut
from fastapi import HTTPException
from typing import List
from app.api import db_manager
from app.api.helpers.product_helper import is_product_id_valid
from app.api.helpers.user_helper import is_user_id_valid
from app.api.log_producer import publish_log

service = "orders"
root = "/orders/"

orders_router = APIRouter()

@orders_router.get("/home")
def root():
    return {"message": "Order Service"}

@orders_router.post("/", status_code=201)
async def create_order(order: OrderIn): # current_user: dict = Depends(is_user_logged_in)

    #check user exists
    if not is_user_id_valid(order.user_id):
        raise HTTPException(status_code=404, detail=f"User not found for id: {order.user_id}")
    
    #check products exist
    for id in order.product_ids:
        if not is_product_id_valid(id):
            raise HTTPException(status_code=404, detail=f"Product not found for id: {id}")
    
    order_id = await db_manager.add_order(order)
    response = {
        'id': order_id,
        **order.dict()
    }
    # publish_log(service, root, "Created a new order")
    return response

@orders_router.get("/", response_model=List[OrderOut])
async def get_all_orders():
#    publish_log(service, root, "Fetched orders data")
   return await db_manager.get_all_orders()

@orders_router.get("/{id}/")
async def get_order(id: int):
    order = await db_manager.get_order(id)
    if not order:
        raise HTTPException(status_code=404, detail="Order not found")
    # publish_log(service, root + "/{id}/", "Fetched order data based on id")
    return order

@orders_router.get("/user/{user_id}/")
async def get_orders_by_user(user_id: int):
    #check user exists
    if not is_user_id_valid(user_id):
        raise HTTPException(status_code=404, detail=f"User not found for id: {user_id}")
    order = await db_manager.get_order_by_user(user_id)
    if not order:
        raise HTTPException(status_code=404, detail=f"Order not found for user id: {user_id}")
    # publish_log(service, root + "/{user_id}/", "Fetched order data based on user id")
    return order