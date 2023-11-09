import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Clothes(SqlAlchemyBase):
    __tablename__ = 'clothes'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String)
    type = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("type.id"))
    season = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("season.id"))
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    types = orm.relationship("Type", backref='clothes')
    seasons = orm.relationship("Season", backref='clothes')
