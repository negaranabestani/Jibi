import uuid

from pydantic import BaseModel, ConfigDict


class ResponseDTO(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)
    responseID: str


class UserDTO(BaseModel):
    username: str
    token: str
    currency: str | None
    calendar: str | None


class UserResponseDTO(ResponseDTO):
    user: UserDTO


class RecordDTO(BaseModel):
    amount: str
    category: str
    date: str
    title: str
    user_id: int
    id: int


class RecordResponseDTO(ResponseDTO):
    record: RecordDTO


class RecordsResponseDTO(ResponseDTO):
    record: []


class CategoryDTO(BaseModel):
    color: str
    icon: str
    title: str
    user_id: int
    id: int


class CategoryResponseDTO(ResponseDTO):
    category: CategoryDTO


class CategoriesResponseDTO(ResponseDTO):
    category: [CategoryDTO]
