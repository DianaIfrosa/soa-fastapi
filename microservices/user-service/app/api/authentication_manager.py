from fastapi import HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from passlib.context import CryptContext
from jose import jwt 
from app.api import db_manager
from app.api.models import UserOut
from pydantic import parse_obj_as

SECRET_KEY = "hello"

#algorithm used for JWT token encoding
ALGORITHM = "HS256"

#context for password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def authenticate_user(username: str, password: str):
    user = await db_manager.get_user_by_username(username)
    if not user:
        return False
    user_model = parse_obj_as(UserOut, user)

    if not pwd_context.verify(password, user_model.password):
        return False
    return user_model

def create_access_token(data: dict):
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return {"username": username}
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")