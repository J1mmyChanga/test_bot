import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Looks(SqlAlchemyBase):
    __tablename__ = 'looks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    style = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("style.id"))
    season = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("season.id"))
    sex = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("sex.id"))
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    styles = orm.relationship("Style", backref='looks')
    seasons = orm.relationship("Season", backref='looks')
    sex_ = orm.relationship("Sex", backref='looks')

    clothes = orm.relationship("Clothes",
                               secondary="look_to_clothes",
                               backref="look")
