from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database
import os

# DATABASE_URI = 'postgresql://postgres:diana123@localhost/soa'
DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

users = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50))
)

database = Database(DATABASE_URI)