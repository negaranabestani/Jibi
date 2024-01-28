from pydantic import BaseModel
from enum import Enum


class RecordType(Enum):
    Income = "Income"
    Expense = "Expense"


class RecordRequestObj(BaseModel):
    title: str | None
    amount: float
    category: str | None
    type: RecordType


class UserRequestBody(BaseModel):
    email: str
    password: str
    username: str
    calendar: str
    currency: str
