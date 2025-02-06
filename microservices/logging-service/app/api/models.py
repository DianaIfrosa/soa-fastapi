from pydantic import BaseModel
from datetime import datetime

#todo: delete?
class Log(BaseModel):
    endpoint: str
    service: str
    timestamp: datetime
    message: str