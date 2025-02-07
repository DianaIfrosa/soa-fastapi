from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.api.models import UserIn, UserOut
from app.api import db_manager
from fastapi.security import OAuth2PasswordRequestForm
from app.api import authentication_manager
from app.api.authentication_manager import pwd_context, get_current_user
from app.api.log_producer import publish_log

users_router = APIRouter()
service = "users"
root = "/users/"

@users_router.get("/home/")
def root():
    return {"message": "User Service"}

@users_router.post("/signup", status_code=201)
async def create_user(user: UserIn):
    user.password = pwd_context.hash(user.password)
    user_id = await db_manager.add_user(user)
    response = {
        'id': user_id,
        **user.dict()
    }
    response.pop("password")
    return response


@users_router.get("/", response_model=List[UserOut])
async def get_all_users(current_user: dict = Depends(get_current_user)):
   if current_user["username"] == "admin": # todo: change it
        # publish_log(service, root, "Fetched all users data")
        return await db_manager.get_all_users()
   else:
       raise HTTPException(status_code=401, detail="You are not allowed!") 
   

#get current user details from authentication token from header
@users_router.get("/me/")
async def get_current_user_details(current_user: dict = Depends(get_current_user)):
    user = await db_manager.get_user_by_username(current_user["username"])
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    # publish_log(service, root + "/me/", "Fetched personal user data")
    return user
    
@users_router.get("/{user_id}/")
async def get_user_by_id(user_id: int):
        user = await db_manager.get_user_by_id(user_id)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        # publish_log(service, root + "/{user_id}/", "Fetched user data based on id")
        return user

#todo: make protected, accessibile only for admin?
@users_router.get("/{username}/")
async def get_user_by_name(username: str, current_user: dict = Depends(get_current_user)):
    if current_user["username"] == "admin": # todo: change it
        user = await db_manager.get_user_by_username(username)
        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        # publish_log(service, root + "/{username}/", "Fetched user data based on username")
        return user
    else:
       raise HTTPException(status_code=401, detail="You are not allowed!") 

@users_router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user: UserOut = await authentication_manager.authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token_data = {"sub": user.username}
    access_token = authentication_manager.create_access_token(token_data)
    # publish_log(service, root + "/login/", "Logged in")
    return {"access_token": access_token, "token_type": "bearer"}