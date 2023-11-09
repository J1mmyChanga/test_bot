import sqlalchemy as sql
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Users(SqlAlchemyBase):
    __tablename__ = 'users'
    id = sql.Column(sql.Integer, primary_key=True, autoincrement=True)
    user_id = sql.Column(sql.String, nullable=False)
    first_name = sql.Column(sql.String, nullable=False)
    last_name = sql.Column(sql.String, nullable=False)