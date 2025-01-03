from pydantic import BaseModel

class UserIn(BaseModel):
    username: str
    password: str

class UserOut(UserIn):
    id: int