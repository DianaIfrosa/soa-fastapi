from fastapi import FastAPI
from app.api.service import logging_router
from app.api.db import metadata, engine, database
from app.api.consumer import consume_logs
import time 
import logging

# metadata.create_all(engine)
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger("my logger")

# app = FastAPI(openapi_url="/api/v1/logs/openapi.json", docs_url="/api/v1/logs/docs")
# # @app.on_event("startup")
# # async def startup():
# #     await init_db()

# # @app.get("/")
# # def root():
# #     return {"message": "Logging service is running"}

# @app.on_event("startup")
# async def startup():
#     await database.connect()

# @app.on_event("shutdown")
# async def shutdown():
#     await database.disconnect()

# app.include_router(logging_router, prefix='/api/v1/logs', tags=['logs'])

# def startup():
#     logger.info("Starting consumer...")
#     # time.sleep(20)
#     consume_logs()

# if __name__ == "__main__":
#     try:
#         startup() # this is not called, fixit, if i move it outside of the if and delete the if it is not awaited
#     except Exception as e:
#         print(f"Exception occurred: {e}")
