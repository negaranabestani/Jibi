import time

from app.api.request_dto import RecordRequestDTO
from app.api.response_dto import *
from app.controller.record_controller import *
from app.exception.api_exception import ApiException
from app.exception.controller_exception import ControllerException
from app.util.general_utils import *


def exception_handler(fun):
    def wrapper(*args, **kwargs):
        try:
            fun(*args, **kwargs)
        except ControllerException as e:
            raise ApiException(e.message, e.status_code)

    return wrapper


@exception_handler
def add_record_service(request: RecordRequestDTO):
    new_record = request.record
    user_id = token_parser(request.token)
    record = Record(new_record.amount, new_record.category, time.asctime(), new_record.title, user_id)
    result: Record = add_record(record)
    response_dto = RecordDTO(amount=result.amount,
                             category=result.category,
                             date=result.date,
                             title=result.title,
                             user_id=result.user_id,
                             id=result.id)
    return RecordResponseDTO(record=response_dto, responseID=str(uuid.uuid4()))


@exception_handler
def edit_record_service(request: RecordRequestDTO):
    new_record = request.record
    user_id = token_parser(request.token)
    record = Record(new_record.amount, new_record.category, time.asctime(), new_record.title, user_id)
    result = edit_record(record, request.record_id)
    response_dto = RecordDTO(amount=result.amount,
                             category=result.category,
                             date=result.date,
                             title=result.title,
                             user_id=result.user_id,
                             id=result.id)
    return RecordResponseDTO(record=response_dto, responseID=str(uuid.uuid4()))


@exception_handler
def delete_record_service(request: RecordRequestDTO):
    delete_record(request.record.record_id)


@exception_handler
def get_records_service(user_id):
    records = []
    for result in get_records(user_id):
        response_dto = RecordDTO(amount=result.amount,
                                 category=result.category,
                                 date=result.date,
                                 title=result.title,
                                 user_id=result.user_id,
                                 id=result.id)
        records.append(response_dto)
    RecordResponseDTO(record=records, responseID=str(uuid.uuid4()))
    return RecordResponseDTO
