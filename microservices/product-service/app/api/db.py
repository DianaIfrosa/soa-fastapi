from sqlalchemy import (Column, Integer, MetaData, String, Table, Float,
                        create_engine, ARRAY)

from databases import Database
import os

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

products = Table(
    'product',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('price', Float)
)

database = Database(DATABASE_URI)