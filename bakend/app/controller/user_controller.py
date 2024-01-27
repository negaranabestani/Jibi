import uuid
from app.entity.person import Person, User
from app.exception.controller_exception import DuplicationException, ValidationException


def login(email, password):
    valid = True
    user_id = ""
    # TODO check input validity form database
    if not valid:
        raise ValidationException("email or password")
    two_step_verification(email)
    return generate_token(user_id)


def generate_token(user_id):
    return user_id + str(uuid.uuid4())


def two_step_verification(email):
    # TODO two step verification
    pass


def sign_up(person: Person):
    duplicated = False
    # TODO check duplication on email
    if duplicated:
        raise DuplicationException("email")
    two_step_verification(person.email)
    # TODO add person to db
    pass
