from datetime import datetime

from sqlalchemy import MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.sql.functions import random
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy.sql.sqltypes import DATETIME
from sqlalchemy.types import Integer, String

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)
_Base = declarative_base(metadata=metadata)


class BaseModel(_Base):
    __abstract__ = True
    created = Column(DATETIME, default=datetime.now)
    modified = Column(DATETIME, default=datetime.now)

    def __init__(self):
        self.created = datetime.now
        self.modified = datetime.now

    def __repr__(self) -> str:
        columns = ", ".join(
            [f"{k}={repr(v)}" for k, v in self.__dict__.items() if not k.startswith("_")]
        )
        return f"<{self.__class__.__name__}({columns})>"


