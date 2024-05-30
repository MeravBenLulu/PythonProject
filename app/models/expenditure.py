
from pydantic import BaseModel


class Expenditure(BaseModel):
    _id: str
    name: str
    amount: int

