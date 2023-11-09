import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Type(SqlAlchemyBase):
    __tablename__ = 'type'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    type = sqlalchemy.Column(sqlalchemy.String)
