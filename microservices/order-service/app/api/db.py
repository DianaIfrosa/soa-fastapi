from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine)

from databases import Database
import os

DATABASE_URI = os.getenv('DATABASE_URI')

engine = create_engine(DATABASE_URI)
metadata = MetaData()

orders = Table(
    'order',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('user_id', Integer),
    Column('product_id', Integer),
    Column('date', String(50)),
    Column('address', String(150))
)

database = Database(DATABASE_URI)