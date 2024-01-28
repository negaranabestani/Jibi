from app.api.request_dto import UserRequestDTO
from app.controller.user_controller import *
from app.exception.controller_exception import *
from app.exception.api_exception import *
from app.entity.person import *
from app.api.response_dto import *


def controller_exception_handler(fun):
    def wrapper(*args, **kwargs):
        try:
            fun(*args, **kwargs)
        except ControllerException as e:
            raise ApiException(e.message, e.status_code)

    return wrapper


@controller_exception_handler
def login_service(email, password):
    token, username = login(email, password)
    response_user = UserDTO(username=username, token=token)
    response = UserResponseDTO(user=response_user, responseID=str(uuid.uuid4()))
    return response


@controller_exception_handler
def sign_up_service(new_user: UserRequestDTO):
    # TODO validate format and set default values if null
    user = User(new_user.email, new_user.password)
    user.currency = new_user.currency
    user.calendar = new_user.calendar
    token = sign_up(user)
    response_user = UserDTO(username=user.username, token=token)
    response = UserResponseDTO(user=response_user, responseID=str(uuid.uuid4()))
    return response
