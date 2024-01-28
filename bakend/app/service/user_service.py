from app.api.request_obj import UserRequestDTO
from app.controller.user_controller import *


def login_service(email, password):
    try:
        login(email,password)
    except

def sign_up_service(new_user: UserRequestDTO):
