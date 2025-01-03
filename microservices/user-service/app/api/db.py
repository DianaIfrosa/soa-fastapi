from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database
import os

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

users = Table(
    'user',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('username', String(50)),
    Column('password', String(80)) #encrypted
)

database = Database(DATABASE_URI)