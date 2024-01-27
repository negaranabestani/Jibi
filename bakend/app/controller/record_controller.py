from app.entity.record import Record
from app.exception.controller_exception import DuplicationException, ValidationException


def add_record(new_record: Record):
    duplicated = False
    record_id = None
    # TODO check name duplication
    if duplicated:
        raise DuplicationException("record name")
    # TODO add record to database
    return record_id


def delete_record(record_id):
    if record_id is None:
        raise ValidationException("record_id")
    # TODO delete record and check for db exception


def edit_record(new_record: Record, record_id):
    if record_id is None:
        raise ValidationException("record_id")
    # TODO update record and check for db exception
