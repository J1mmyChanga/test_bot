import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Users(SqlAlchemyBase, UserMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    sex = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("sex.id"))
    nickname = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String)
    image = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    sex_ = orm.relationship("Sex", backref="users")

    favourite_looks = orm.relationship("Looks",
                                       secondary="user_to_favourite_looks",
                                       backref="user_looks")

    favourite_custom_looks = orm.relationship("CustomLooks",
                                              secondary="user_to_favourite_custom_looks",
                                              backref="user_custom")

    clothes = orm.relationship("Clothes",
                               secondary="user_to_clothes",
                               backref="user")

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)
