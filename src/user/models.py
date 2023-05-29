import uuid
from datetime import datetime

from fastapi_users.db import (
    SQLAlchemyBaseUserTable
)
from sqlalchemy import Column, Boolean, String, TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID

from src.db.models import BaseModel


class User(SQLAlchemyBaseUserTable[uuid.UUID], BaseModel):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(length=256), unique=True, index=True, nullable=False)
    username = Column(String(length=256), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)
    hashed_password = Column(String(length=1024), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_superuser = Column(Boolean, default=False, nullable=False)
    is_verified = Column(Boolean, default=False, nullable=False)
