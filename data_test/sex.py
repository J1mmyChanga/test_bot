import sqlalchemy

from .db_session import SqlAlchemyBase


class Sex(SqlAlchemyBase):
    __tablename__ = 'sex'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    sex = sqlalchemy.Column(sqlalchemy.String)
