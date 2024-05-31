import time

from bakend.app.api.request_dto import RecordRequestDTO, CategoryRequestDTO
from bakend.app.api.response_dto import *
from bakend.app.controller.record_controller import *
from bakend.app.exception.api_exception import ApiException
from bakend.app.exception.controller_exception import ControllerException
from bakend.app.util.general_utils import *


def exception_handler(fun):
    def wrapper(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except ControllerException as e:
            raise ApiException(e.message, e.status_code)

    return wrapper


@exception_handler
def add_record_service(request: RecordRequestDTO, token):
    new_record = request.record
    user_id = token_parser(token)
    record = Record(new_record.amount, new_record.category, time.asctime(), new_record.title, user_id, str(new_record.type.value))
    result: Record = add_record(record, user_id)
    response_dto = RecordDTO(amount=str(result.amount),
                             category=result.category_id,
                             date=result.date,
                             title=result.title,
                             user_id=result.user_id,
                             type=result.type,
                             id=result.id)
    return RecordResponseDTO(record=response_dto, responseID=str(uuid.uuid4()))


@exception_handler
def edit_record_service(request: RecordRequestDTO, token):
    new_record = request.record
    user_id = token_parser(token)
    record = Record(new_record.amount, new_record.category, time.asctime(), new_record.title, user_id, str(new_record.type.value))
    record.id = request.record_id
    result: Record = edit_record(record, request.record_id, user_id)
    response_dto = RecordDTO(amount=str(result.amount),
                             category=result.category_id,
                             date=str(result.date),
                             title=str(result.title),
                             user_id=result.user_id,
                             type=result.type,
                             id=result.id)
    return RecordResponseDTO(record=response_dto, responseID=str(uuid.uuid4()))


@exception_handler
def delete_record_service(record_id):
    remove_record(record_id)
    return ResponseDTO(responseID=str(uuid.uuid4()))


@exception_handler
def get_records_service(user_id):
    records = []
    record_list = get_records(user_id)

    for rec in record_list:
        result: Record = rec
        response_dto = RecordDTO(amount=str(result.amount),
                                 category=result.category_id,
                                 date=str(result.date),
                                 title=str(result.title),
                                 user_id=result.user_id,
                                 type=result.type,
                                 id=result.id)
        records.append(response_dto)
    return RecordsResponseDTO(record=records, responseID=str(uuid.uuid4()))


@exception_handler
def add_category_service(request: CategoryRequestDTO, token):
    new_category = request.category
    user_id = token_parser(token)
    cat = Category(new_category.color, new_category.icon, new_category.title, user_id)
    result: Category = add_category(cat, user_id)
    response_dto = CategoryDTO(color=str(result.color),
                               icon=str(result.icon),
                               title=str(result.title),
                               user_id=result.user_id,
                               id=result.id)
    return CategoryResponseDTO(category=response_dto, responseID=str(uuid.uuid4()))


@exception_handler
def edit_category_service(request: CategoryRequestDTO, token):
    new_category = request.category
    user_id = token_parser(token)
    cat = Category(new_category.color, new_category.icon, new_category.title, user_id)
    cat.id = new_category.id
    result: Category = edit_category(cat, cat.id, user_id)
    response_dto = CategoryDTO(color=str(result.color),
                               icon=str(result.icon),
                               title=str(result.title),
                               user_id=result.user_id,
                               id=result.id)
    return CategoryResponseDTO(category=response_dto, responseID=str(uuid.uuid4()))


@exception_handler
def delete_category_service(cat_id):
    remove_category(cat_id)
    return ResponseDTO(responseID=str(uuid.uuid4()))


@exception_handler
def get_categories_service(user_id):
    categories = []
    for result in get_categories(user_id):
        response_dto = CategoryDTO(color=str(result.color),
                                   icon=str(result.icon),
                                   title=str(result.title),
                                   user_id=result.user_id,
                                   id=result.id)
        categories.append(response_dto)
    return CategoriesResponseDTO(category=categories, responseID=str(uuid.uuid4()))
