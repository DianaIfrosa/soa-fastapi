from app.api.db import logs, database

async def get_all_logs():
    query = logs.select()
    return await database.fetch_all(query=query)