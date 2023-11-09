import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class CustomLooks(SqlAlchemyBase):
    __tablename__ = 'custom_looks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    style = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("style.id"))
    season = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("season.id"))
    sex = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("sex.id"))
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))

    styles = orm.relationship("Style", backref='custom_looks')
    seasons = orm.relationship("Season", backref='custom_looks')
    sex_ = orm.relationship("Sex", backref='custom_looks')
    users = orm.relationship("Users", backref='custom_looks')

    clothes = orm.relationship("Clothes",
                               secondary="custom_looks_to_clothes",
                               backref="custom_looks")