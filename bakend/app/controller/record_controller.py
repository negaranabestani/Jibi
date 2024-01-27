from app.entity.record import Record
from app.exception.controller_exception import DuplicationException


def add_record(new_record: Record):
    duplicated = False
    record_id = None
    # TODO check name duplication
    if duplicated:
        raise DuplicationException("record name")
    # TODO add record to database
    return record_id
