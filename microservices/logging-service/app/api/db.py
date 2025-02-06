from sqlalchemy import (Column, Integer, MetaData, String, Table, Float, TIMESTAMP,
                        func, create_engine, ARRAY)

from databases import Database
import os

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

logs = Table(
    'audit',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('endpoint', String(150)),
    Column('service', String(50)),
    Column('timestamp', TIMESTAMP, server_default=func.now()),
    Column('message', String(200))
)

database = Database(DATABASE_URI)

# from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
# from sqlalchemy.orm import sessionmaker, declarative_base
# import os
# from sqlalchemy import Column, Integer, String, TIMESTAMP, func

# DATABASE_URI = os.getenv('DATABASE_URI')

# engine = create_async_engine(DATABASE_URI, echo=True)
# SessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
# Base = declarative_base()

# class AuditLog(Base):
#     __tablename__ = "audit_logs"

#     id = Column(Integer, primary_key=True, index=True)
#     service = Column(String, index=True)
#     endpoint = Column(String, index=True)
#     timestamp = Column(TIMESTAMP, server_default=func.now())
#     message = Column(String)

# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)