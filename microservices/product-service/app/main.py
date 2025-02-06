from fastapi import FastAPI
from app.api.products import products_router
from app.api.db import metadata, database, engine
from fastapi.middleware.cors import CORSMiddleware

metadata.create_all(engine)

app = FastAPI(openapi_url="/api/v1/products/openapi.json", docs_url="/api/v1/products/docs")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

app.include_router(products_router, prefix='/api/v1/products', tags=['products'])
