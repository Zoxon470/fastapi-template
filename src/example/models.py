from sqlalchemy import Column, String

from src.db.models import BaseModel


class Example(BaseModel):
    __tablename__ = "example"

    name = Column(String(255), nullable=False)
