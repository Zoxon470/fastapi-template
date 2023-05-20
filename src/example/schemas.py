from pydantic import BaseModel


class Example(BaseModel):
    id: int

    class Config:
        orm_mode = True
