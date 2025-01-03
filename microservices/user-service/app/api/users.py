from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.api.models import UserIn, UserOut
from app.api import db_manager
from fastapi.security import OAuth2PasswordRequestForm
from app.api import authentication_manager
from app.api.authentication_manager import pwd_context

users_router = APIRouter()

@users_router.get("/home/")
def root():
    return {"message": "User Service"}

@users_router.post("/", status_code=201)
async def create_user(user: UserIn):
    user.password = pwd_context.hash(user.password)
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
async def get_user_by_id(user_id: int):
    user = await db_manager.get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@users_router.get("/{username}/")
async def get_user_by_name(username: str):
    user = await db_manager.get_user_by_username(username)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@users_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user: UserOut = await authentication_manager.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token_data = {"sub": user.username}
    access_token = authentication_manager.create_access_token(token_data)
    return {"access_token": access_token, "token_type": "bearer"}