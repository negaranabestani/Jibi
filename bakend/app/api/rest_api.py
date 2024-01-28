from typing import Annotated

from fastapi import FastAPI, Header, Request
from fastapi.responses import JSONResponse

from app.api.request_dto import *
from app.exception.api_exception import ApiException
from app.service.user_service import *
from app.service.record_service import *
from app.util.general_utils import *

app = FastAPI()

base_url = "/jibi"


def login_required(func):
    def wrapper(*args, **kwargs):
        token = kwargs.get("x_token")
        if token is None:
            raise ApiException("null token", 401)
        func(*args, **kwargs)

    return wrapper


@app.post(f"{base_url}" + "/signup/{email}")
async def sign_up(email, username, password):
    request_dto = UserDTO(email=email, username=username, password=password, calendar=None, currency=None)
    request = UserRequestDTO(user=request_dto, requestID=uuid.uuid4())
    return sign_up_service(request)


@app.post(f"{base_url}" + "/signin/{email}")
async def sign_in(email, password):
    request_dto = UserDTO(email=email, username=None, password=password, calendar=None, currency=None)
    request = UserRequestDTO(user=request_dto, requestID=uuid.uuid4())
    return login_service(request)


@login_required
@app.post(f"{base_url}" + "/record/")
async def record_insertion(record: RecordRequestDTO, x_token: Annotated[str | None, Header()] = None):
    return add_record_service(record)


@login_required
@app.put(f"{base_url}" + "/record/")
async def record_edition(record: RecordRequestDTO, x_token: Annotated[str | None, Header()] = None):
    return edit_record_service(record)


@login_required
@app.delete(f"{base_url}" + "/record/{record_id}")
async def record_deletion(record_id, x_token: Annotated[str | None, Header()] = None):
    return delete_record(record_id)


@login_required
@app.get(f"{base_url}" + "/record/")
async def record_deletion(x_token: Annotated[str | None, Header()] = None):
    return get_records(token_parser(x_token))


@app.exception_handler(ApiException)
async def api_exception_handler(request: Request, exc: ApiException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"{exc.message} ", "request": f"{request.body()}"},
    )
