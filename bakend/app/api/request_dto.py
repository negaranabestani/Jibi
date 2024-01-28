import uuid

from pydantic import BaseModel
from enum import Enum


class RecordType(Enum):
    Income = "Income"
    Expense = "Expense"


class RequestDTO(BaseModel):
    requestID: uuid
    token: str


class RecordDTO(BaseModel):
    title: str | None
    amount: float
    category: str | None
    type: RecordType
    record_id: str | None


class RecordRequestDTO(RequestDTO):
    record: RecordDTO


class UserDTO:
    email: str
    password: str
    username: str | None
    calendar: str | None
    currency: str | None


class UserRequestDTO(RequestDTO):
    user: UserDTO
