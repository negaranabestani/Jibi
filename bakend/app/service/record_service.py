import time

from app.api.request_dto import RecordRequestDTO, CategoryRequestDTO
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


@exception_handler
def add_category_service(request: CategoryRequestDTO):
    new_category = request.category
    user_id = token_parser(request.token)
    cat = Category(new_category.color, new_category.icon, new_category.title, user_id)
    result: Category = add_category(cat)
    response_dto = CategoryDTO(color=result.color,
                               icon=result.icon,
                               title=result.title,
                               user_id=result.user_id,
                               id=result.id)
    return CategoryResponseDTO(category=response_dto, responseID=str(uuid.uuid4()))


@exception_handler
def edit_category_service(request: CategoryRequestDTO):
    new_category = request.category
    user_id = token_parser(request.token)
    cat = Category(new_category.color, new_category.icon, new_category.title, user_id)
    result: Category = edit_category(cat, cat.id)
    response_dto = CategoryDTO(color=result.color,
                               icon=result.icon,
                               title=result.title,
                               user_id=result.user_id,
                               id=result.id)
    return CategoryResponseDTO(category=response_dto, responseID=str(uuid.uuid4()))


@exception_handler
def delete_category_service(request: CategoryRequestDTO):
    delete_category(request.category.id)


@exception_handler
def get_categories_service(user_id):
    categories = []
    for result in get_categories(user_id):
        response_dto = CategoryDTO(color=result.color,
                                   icon=result.icon,
                                   title=result.title,
                                   user_id=result.user_id,
                                   id=result.id)
        categories.append(response_dto)
    CategoryResponseDTO(category=categories, responseID=str(uuid.uuid4()))
    return RecordResponseDTO
