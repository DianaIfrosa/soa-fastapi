from fastapi import APIRouter
from fastapi import HTTPException
from typing import List
from app.api.models import UserIn, UserOut
from app.api import db_manager

users_router = APIRouter()

@users_router.get("/home/")
def root():
    return {"message": "User Service"}

@users_router.post("/", status_code=201)
async def create_user(user: UserIn):
    user_id = await db_manager.add_user(user)
    response = {
        'id': user_id,
        **user.dict()
    }

    return response


@users_router.get("/", response_model=List[UserOut])
async def get_all_users():
   return await db_manager.get_all_users()
    
@users_router.get("/{user_id}/")
async def get_user(user_id: int):
    user = await db_manager.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user