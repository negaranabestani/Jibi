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


def add_category(new_category: Category):
    if record_exist(new_category.title):
        raise DuplicationException("record name")
    return create_category(new_category)


def delete_category(cat_id):
    try:
        delete_category(cat_id)
    except ObjectDeletedError:
        raise ValidationException("record_id")


def edit_category(new_category: Category, cat_id):
    if cat_id is None:
        raise ValidationException("record_id")
    try:
        return edit_category(new_category, cat_id)
    except ObjectDeletedError:
        raise ValidationException("record_id")


def get_categories(user_id):
    try:
        return select_categories(user_id)
    except ObjectDeletedError:
        raise ValidationException("user_id")
