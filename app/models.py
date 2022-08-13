from datetime import datetime
import uuid

from sqlalchemy import (Column, MetaData, func, UniqueConstraint, ForeignKey)
from sqlalchemy.types import Integer, String, DateTime
from sqlalchemy.orm import declarative_mixin, declared_attr, relationship, declarative_base

convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}
metadata = MetaData(naming_convention=convention)


class Base:
    created_at = Column(DateTime, default=func.now(), nullable=False)
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now(), nullable=False)

    def __repr__(self) -> str:
        columns = ", ".join([f"{k}={repr(v)}" for k, v in self.__dict__.items() if not k.startswith("_")])
        return f"<{self.__class__.__name__}({columns})>"


BaseModel = declarative_base(metadata=metadata, cls=Base)


class Tenant(BaseModel):
    __tablename__ = "tenant"
    __table_args__ = (UniqueConstraint("name"), {})
    id = Column(String(36), primary_key=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)

    users = relationship(
        "User",
        order_by="User.id",
        back_populates="tenant",
        cascade="all",
        passive_deletes=True,
    )


@declarative_mixin
class HasTenantMixin:
    id = Column(Integer, primary_key=True)

    @declared_attr
    def tenant_id(cls):
        return Column(String(36), ForeignKey("tenant.id", ondelete="CASCADE"), nullable=False)

    @declared_attr
    def tenant(cls):
        return relationship("Tenant")


class User(HasTenantMixin, BaseModel):
    __tablename__ = "users"
    __table_args__ = (UniqueConstraint("name"), {})
    name = Column(String(255), nullable=False)
