from typing import Any

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy.ext.declarative import declarative_base

Base: Any = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(Integer, nullable=False, primary_key=True)
