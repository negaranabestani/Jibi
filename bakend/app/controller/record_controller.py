from sqlalchemy.orm.exc import ObjectDeletedError
from app.db.database_connectivity import *
from app.exception.controller_exception import DuplicationException, ValidationException


def add_record(new_record: Record):
    if record_exist(new_record.title):
        raise DuplicationException("record name")
    return create_record(new_record)


def delete_record(record_id):
    try:
        delete_record(record_id)
    except ObjectDeletedError:
        raise ValidationException("record_id")


def edit_record(new_record: Record, record_id):
    if record_id is None:
        raise ValidationException("record_id")
    try:
        return edit_record(new_record, record_id)
    except ObjectDeletedError:
        raise ValidationException("record_id")


def get_records(user_id):
    try:
        return select_records(user_id)
    except ObjectDeletedError:
        raise ValidationException("user_id")
