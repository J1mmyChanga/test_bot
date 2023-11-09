import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Season(SqlAlchemyBase):
    __tablename__ = 'season'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    season = sqlalchemy.Column(sqlalchemy.String)
    look_season = sqlalchemy.Column(sqlalchemy.String)
