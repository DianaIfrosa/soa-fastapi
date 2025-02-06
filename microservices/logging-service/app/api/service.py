from fastapi import APIRouter
from fastapi import HTTPException
from typing import List
from app.api.models import Log
from app.api import db_manager

logging_router = APIRouter()

@logging_router.get("/home/")
def root():
    return {"message": "Logging Service"}

@logging_router.get("/") # response_model=List[Log]
async def get_all_logs():
   return await db_manager.get_all_logs()