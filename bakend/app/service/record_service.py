import time

from app.api.request_dto import RecordRequestDTO
from app.api.response_dto import *
from app.exception.api_exception import ApiException
from app.exception.controller_exception import ControllerException
from app.entity.record import *
from app.util.general_utils import *
from app.controller.record_controller import *


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
    add_record(record)


@exception_handler
def edit_record_service(request: RecordRequestDTO):
    new_record = request.record
    user_id = token_parser(request.token)
    record = Record(new_record.amount, new_record.category, time.asctime(), new_record.title, user_id)
    edit_record(record, request.record_id)


@exception_handler
def delete_record_service(request: RecordRequestDTO):
    delete_record(request.record.record_id)
