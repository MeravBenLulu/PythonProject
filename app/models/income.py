from datetime import datetime

from pydantic import BaseModel


class Income(BaseModel):
    _id: str
    name: str
    amount: int

