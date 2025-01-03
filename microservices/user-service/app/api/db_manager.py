from app.api.models import UserIn
from app.api.db import users, database

async def add_user(payload: UserIn):
    query = users.insert().values(**payload.dict())
    return await database.execute(query=query)

async def get_all_users():
    query = users.select()
    return await database.fetch_all(query=query)

async def get_user_by_id(id: int):
    query = users.select(users.c.id==id)
    return await database.fetch_one(query=query)

async def get_user_by_username(username: str):
    query = users.select(users.c.username==username)
    return await database.fetch_one(query=query)