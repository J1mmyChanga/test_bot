import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Style(SqlAlchemyBase):
    __tablename__ = 'style'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    style = sqlalchemy.Column(sqlalchemy.String)
