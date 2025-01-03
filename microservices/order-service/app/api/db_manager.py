from app.api.models import OrderIn
from app.api.db import orders, database

async def add_order(payload: OrderIn):
    query = orders.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_orders():
    query = orders.select()
    return await database.fetch_all(query=query)

async def get_order(id: int):
    query = orders.select(orders.c.id==id)
    return await database.fetch_one(query=query)

async def get_order_by_user(id: int):
    query = orders.select(orders.c.user_id==id)
    return await database.fetch_one(query=query)