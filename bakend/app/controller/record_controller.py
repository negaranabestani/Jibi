from sqlalchemy.orm.exc import ObjectDeletedError
from app.db.database_connectivity import *
from app.exception.controller_exception import DuplicationException, ValidationException


def add_record(new_record: Record, user_id):
    jibi_logger.info(new_record.category)
    if new_record.category == None or not category_exist_id(new_record.category):
        raise ValidationException("category_id")
    if record_exist(new_record.title, user_id):
        raise DuplicationException("record name")
    return create_record(new_record)


def remove_record(record_id):
    try:
        delete_record(record_id)
    except ObjectDeletedError:
        raise ValidationException("record_id")


def edit_record(new_record: Record, record_id, user_id):
    if record_id is None:
        raise ValidationException("record_id")
    try:
        if record_exist(new_record.title, user_id):
            raise DuplicationException("record name")
        return update_record(new_record)
    except ObjectDeletedError:
        raise ValidationException("record_id")


def get_records(user_id):
    try:
        return select_records(user_id)
    except ObjectDeletedError:
        raise ValidationException("user_id")


def add_category(new_category: Category, user_id):
    if category_exist(new_category.title, user_id):
        raise DuplicationException("category name")
    return create_category(new_category)


def delete_category(cat_id):
    try:
        delete_category(cat_id)
    except ObjectDeletedError:
        raise ValidationException("category_id")


def edit_category(new_category: Category, cat_id, user_id):
    if cat_id is None:
        raise ValidationException("category_id")
    try:
        if category_exist(new_category.title, user_id):
            raise DuplicationException("category name")
        return update_category(new_category)
    except ObjectDeletedError:
        raise ValidationException("category_id")


def get_categories(user_id):
    try:
        return select_categories(user_id)
    except ObjectDeletedError:
        raise ValidationException("user_id")
