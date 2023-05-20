from db.models import BaseModel
from datetime import datetime
from sqlalchemy import Column, DateTime


class TimestampMixin(BaseModel):
    created_at = Column(DateTime, nullable=False, default=datetime.now)
    updated_at = Column(
        DateTime, nullable=False, default=datetime.now, onupdate=datetime.now
    )
