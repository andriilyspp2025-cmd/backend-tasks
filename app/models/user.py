from sqlalchemy import Column, String, Boolean
from app.db.db import Base
from app.models.mixins import UUIDMixin, TimestampMixin

class User(UUIDMixin, TimestampMixin, Base):
    __tablename__ = "users"

    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    username = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
