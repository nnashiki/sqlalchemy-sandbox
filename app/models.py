from datetime import datetime

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column, ForeignKey
from sqlalchemy.sql.functions import random
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy.sql.sqltypes import DATETIME
from sqlalchemy.types import Integer, String

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True
    created = Column(DATETIME, default=datetime.now)
    modified = Column(DATETIME, default=datetime.now)

    def __init__(self):
        self.created = datetime.now
        self.modified = datetime.now


class User(BaseModel):
    __tablename__ = "user_account"

    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user", cascade="all, delete-orphan")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(BaseModel):
    __tablename__ = "address"

    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
