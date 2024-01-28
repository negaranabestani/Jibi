import uuid

from pydantic import BaseModel


class ResponseDTO(BaseModel):
    responseID: uuid


class UserDTO(BaseModel):
    username: str
    token: str


class UserResponseDTO(ResponseDTO):
    user: UserDTO


class RecordDTO(BaseModel):
    amount: str
    category: str
    date: str
    title: str
    user_id: str
    id: str


class RecordResponseDTO(ResponseDTO):
    record: RecordDTO
