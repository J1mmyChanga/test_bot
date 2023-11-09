import sqlalchemy

from .db_session import SqlAlchemyBase

association_table_1 = sqlalchemy.Table(
    "user_to_favourite_looks",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("user", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("look", sqlalchemy.Integer, sqlalchemy.ForeignKey("looks.id")))

association_table_2 = sqlalchemy.Table(
    "user_to_clothes",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("user", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("clothes", sqlalchemy.Integer, sqlalchemy.ForeignKey("clothes.id")))

association_table_3 = sqlalchemy.Table(
    "look_to_clothes",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("look", sqlalchemy.Integer, sqlalchemy.ForeignKey("looks.id")),
    sqlalchemy.Column("clothes", sqlalchemy.Integer, sqlalchemy.ForeignKey("clothes.id")))

association_table_4 = sqlalchemy.Table(
    "custom_looks_to_clothes",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("custom_look", sqlalchemy.Integer, sqlalchemy.ForeignKey("custom_looks.id")),
    sqlalchemy.Column("clothes", sqlalchemy.Integer, sqlalchemy.ForeignKey("clothes.id")))

association_table_5 = sqlalchemy.Table(
    "user_to_favourite_custom_looks",
    SqlAlchemyBase.metadata,
    sqlalchemy.Column("user", sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id")),
    sqlalchemy.Column("custom_look", sqlalchemy.Integer, sqlalchemy.ForeignKey("custom_looks.id")))
