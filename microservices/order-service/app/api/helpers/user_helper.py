import os
import httpx
# from fastapi import HTTPException, Depends
# from fastapi.security import OAuth2PasswordBearer

USER_SERVICE_HOST_URL = 'http://localhost:8001/api/v1/users/'
url_user = os.environ.get('USER_SERVICE_HOST_URL') or USER_SERVICE_HOST_URL
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def is_user_id_valid(id: int):
    r = httpx.get(f'{url_user}{id}')
    return True if r.status_code == 200 else False

# async def is_user_logged_in(authorization: str):
#     if not authorization.startswith("Bearer "):
#         raise HTTPException(status_code=401, detail="Invalid token format")
    
#     token = authorization.split(" ")[1]
#     async with httpx.AsyncClient() as client:
#         response = await client.post(f'{url_user}{"validate-token/"}', json={"token": token})
#         if response.status_code != 200:
#             raise HTTPException(status_code=401, detail="Invalid or expired token")
#         return response.json()
