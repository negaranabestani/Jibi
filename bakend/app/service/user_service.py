from app.api.request_dto import UserRequestDTO
from app.controller.user_controller import *
from app.exception.controller_exception import *
from app.exception.api_exception import *
from app.entity.person import *
from app.api.response_dto import *
from app.config.logger import jibi_logger
from app.util.general_utils import token_parser


def exception_handler(fun):
    def wrapper(*args, **kwargs):
        try:
            return fun(*args, **kwargs)
        except ControllerException as e:
            raise ApiException(e.message, e.status_code)

    return wrapper


@exception_handler
def login_service(email, password):
    token, user = login(email, password)
    response_user = UserDTO(username=user.username, calendar=user.calendar, currency=user.currency, token=token)
    response = UserResponseDTO(user=response_user, responseID=str(uuid.uuid4()))
    return response


@exception_handler
def sign_up_service(new_user: UserRequestDTO):
    if new_user.user.username == "":
        raise ValidationException("username")
    if new_user.user.password == "":
        raise ValidationException("password")
    # TODO validate format and set default values if null
    x_user = User(new_user.user.email, new_user.user.password, new_user.user.username)
    x_user.currency = new_user.user.currency
    x_user.calendar = new_user.user.calendar
    token, user = sign_up(x_user)
    response_user = UserDTO(username=user.username, calendar=user.calendar, currency=user.currency, token=token)
    response = UserResponseDTO(user=response_user, responseID=str(uuid.uuid4()))
    jibi_logger.info(dict(response))
    return response


@exception_handler
def update_settings_service(user: UserRequestDTO, token):
    x_user = User(user.user.email, user.user.password)
    x_user.currency = user.user.currency
    x_user.calendar = user.user.calendar
    x_user.user_id = token_parser(token)
    result = edit_settings(x_user)
    response_user = UserDTO(username=result.username, calendar=result.calendar, currency=result.currency)
    response = UserResponseDTO(user=response_user, responseID=str(uuid.uuid4()))
    return response
