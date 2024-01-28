from pydantic import BaseModel
from enum import Enum


class RecordType(Enum):
    Income = "Income"
    Expense = "Expense"


class RecordRequestDTO(BaseModel):
    title: str | None
    amount: float
    category: str | None
    type: RecordType


class UserRequestDTO(BaseModel):
    email: str
    password: str
    username: str | None
    calendar: str | None
    currency: str | None
