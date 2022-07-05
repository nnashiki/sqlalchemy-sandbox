from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.schema import ForeignKey
from sqlalchemy.sql.functions import random
from sqlalchemy.sql.schema import UniqueConstraint
from sqlalchemy.sql.sqltypes import DATETIME
from sqlalchemy.types import Integer, String

from datetime import datetime

Base=declarative_base()

class BaseModel(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)
    created = Column(DATETIME, default=datetime.now)
    modified = Column(DATETIME, default=datetime.now)

    def __init__(self):
        self.created = datetime.now
        self.modified = datetime.now

class User(BaseModel):
    """
    service users.
    """
    __tablename__ = "users"
    email = Column(String(255), unique=True)
    password = Column(String(255))

    def __init__(self, email, password):
        self.email = email
        self.password = password

class Match(BaseModel):
    __tablename__ = "matches"
    seed = Column(Integer, nullable=False)

    def __init__(self):
        self.seed = random.randint()

class MatchUser(BaseModel):
    __table_args__= ((UniqueConstraint("match_id", "user_id"), ))
    __tablename__ = "match_users"
    match_id = Column(Integer, ForeignKey("matches.id", onupdate="cascade", ondelete="cascade"))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    def __init__(self, match_id, user_id):
        self.match_id = match_id
        self.user_id = user_id

class MatchTurn(BaseModel):
    __tablename__ = "match_turns"
    id = Column(Integer, primary_key=True, autoincrement=True)
    match_id = Column(Integer, ForeignKey("matches.id", onupdate="cascade", ondelete="cascade"))
    no = Column(Integer, nullable=False)

    def __init__(self, match_id, no):
        self.match_id = match_id
        self.no = no
