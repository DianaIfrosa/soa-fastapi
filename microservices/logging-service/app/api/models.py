from pydantic import BaseModel
from datetime import datetime

class Log(BaseModel):
    endpoint: str
    service: str
    timestamp: datetime
    message: str