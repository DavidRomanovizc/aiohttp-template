from sqlalchemy import (
    Table, Integer, VARCHAR, MetaData, Column
)

__all__ = ('template',)

meta = MetaData()

template = Table(
    'template', meta,
    Column('id', Integer, primary_key=True),
    Column('username', VARCHAR, nullable=True)
)
