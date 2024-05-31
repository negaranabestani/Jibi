import uuid
from bakend.app.exception.controller_exception import DuplicationException, ValidationException
from bakend.app.db.database_connectivity import *
from sqlalchemy.orm.exc import ObjectDeletedError
from bakend.app.config.logger import jibi_logger


def login(email, password):
    try:
        user = get_user(email, password)
        if user is None:
            raise ValidationException("email or password")
    except ObjectDeletedError:
        raise ValidationException("email or password")
    two_step_verification(email)
    return generate_token(user.user_id), user


def generate_token(user_id):
    # TODO check for existing token for user
    return str(user_id) + "::" + str(uuid.uuid4())


def two_step_verification(email):
    # TODO two-step verification
    pass


def sign_up(person: User):
    duplicated = user_exist(person.email)
    if duplicated:
        raise DuplicationException("email")
    two_step_verification(person.email)
    user = create_user(person)
    # jibi_logger.info(str(user.email))
    return generate_token(user.user_id), user


def edit_settings(user: User):
    try:
        return update_user(user)
    except ObjectDeletedError:
        raise ValidationException("email or password")
