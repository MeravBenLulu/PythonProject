from pydantic import BaseModel


class User(BaseModel):
    _id: str
    name: str
    password: str
    age: int
    city: str
