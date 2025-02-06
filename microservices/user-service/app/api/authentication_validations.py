from fastapi import APIRouter, HTTPException, Depends
from jose import jwt, JWTError
from app.api.authentication_manager import SECRET_KEY, ALGORITHM

auth_router = APIRouter()

@auth_router.post("/validate-token/")
async def validate_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        return {"username": username}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")