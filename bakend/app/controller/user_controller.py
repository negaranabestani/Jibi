import uuid
from app.exception.controller_exception import DuplicationException, ValidationException
from app.db.database_connectivity import *
from sqlalchemy.orm.exc import ObjectDeletedError


def login(email, password):
    try:
        user = get_user(email, password)
    except ObjectDeletedError:
        raise ValidationException("email or password")
    two_step_verification(email)
    return generate_token(user.user_id), user


def generate_token(user_id):
    # TODO check for existing token for user
    return user_id + "::" + str(uuid.uuid4())


def two_step_verification(email):
    # TODO two step verification
    pass


def sign_up(person: User):
    duplicated = user_exist(person.email)
    if duplicated:
        raise DuplicationException("email")
    two_step_verification(person.email)
    user = create_user(person)
    return generate_token(user.user_id), user
