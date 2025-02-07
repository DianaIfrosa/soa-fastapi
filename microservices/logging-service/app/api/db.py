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