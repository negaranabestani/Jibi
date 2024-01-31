import uuid

from pydantic import BaseModel, ConfigDict
from enum import Enum


class RecordType(Enum):
    Income = "Income"
    Expense = "Expense"


class RequestDTO(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    requestID: str | None


class RecordDTO(BaseModel):
    title: str | None
    amount: float
    category: int
    type: RecordType


class RecordRequestDTO(RequestDTO):
    record: RecordDTO
    record_id: int | None


class UserRDTO(BaseModel):
    email: str
    password: str
    username: str | None
    calendar: str | None
    currency: str | None


class UserRequestDTO(RequestDTO):
    user: UserRDTO


class CategoryDTO(BaseModel):
    color: str | None
    icon: str | None
    title: str
    id: int | None


class CategoryRequestDTO(RequestDTO):
    category: CategoryDTO
