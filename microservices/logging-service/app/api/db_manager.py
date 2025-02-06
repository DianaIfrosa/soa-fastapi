from app.api.db import logs, database
from app.api.models import Log

async def get_all_logs():
    query = logs.select()
    return await database.fetch_all(query=query)

def add_log(payload: Log):
    try:
        query = logs.insert().values(**payload.dict())
        database.execute(query=query)
        print(f"Logged: {payload}")
    except Exception as e:
        print(f"Error inserting log into database: {e}")
