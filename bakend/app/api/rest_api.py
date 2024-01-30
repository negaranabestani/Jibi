import sys
# import uvicorn as uvicorn
from typing import Annotated
from request_dto import *

sys.path.append('../../')
from uvicorn import run
from fastapi import FastAPI, Header, Request
from fastapi.responses import JSONResponse
from app.exception.api_exception import ApiException
from app.service.user_service import *
from app.service.record_service import *
from app.util.general_utils import *
from app.config.logger import jibi_logger

app = FastAPI()

base_url = "/jibi"


def login_required(func):
    def wrapper(*args, **kwargs):
        token = kwargs.get("x_token")
        if token is None:
            raise ApiException("null token", 401)
        func(*args, **kwargs)

    return wrapper


@app.post(f"{base_url}" + "/signup/{email}", response_model=UserResponseDTO)
async def sign_up(email, username, password):
    # jibi_logger.info(username)
    # jibi_logger.info(password)
    request_dto = UserRDTO(email=email, username=username, password=password, calendar=None, currency=None)
    request = UserRequestDTO(user=request_dto.model_dump(), requestID=str(uuid.uuid4()), token=None)
    response = sign_up_service(request)
    jibi_logger.info(response)
    return response


@app.post(f"{base_url}" + "/signin/{email}", response_model=UserResponseDTO)
async def sign_in(email, password):
    # request_dto = UserRDTO(email=email, username=None, password=password, calendar=None, currency=None)
    # request = UserRequestDTO(user=request_dto.model_dump(), requestID=str(uuid.uuid4()), token=None)
    return login_service(email, password)


@login_required
@app.post(f"{base_url}" + "/record/", response_model=RecordsResponseDTO)
async def record_insertion(record: RecordRequestDTO, x_token: Annotated[str | None, Header()] = None):
    jibi_logger.info(dict(record))
    record.requestID = str(uuid.uuid4())
    return add_record_service(record, x_token)


@login_required
@app.put(f"{base_url}" + "/setting/")
async def setting_edition(user: UserRequestDTO, x_token: Annotated[str | None, Header()] = None):
    return update_settings_service(user, x_token)


@login_required
@app.put(f"{base_url}" + "/record/")
async def record_edition(record: RecordRequestDTO, x_token: Annotated[str | None, Header()] = None):
    return edit_record_service(record, x_token)


@login_required
@app.delete(f"{base_url}" + "/record/{record_id}", response_model=ResponseDTO)
async def record_deletion(record_id, x_token: str = Header(None)):
    res = delete_record_service(record_id, x_token)
    jibi_logger.info(dict(res))
    return res


@login_required
@app.get(f"{base_url}" + "/record/")
async def record_list(x_token: str = Header(None)):
     return get_records_service(token_parser(x_token))


@login_required
@app.post(f"{base_url}" + "/category/")
async def category_insertion(category: CategoryRequestDTO, x_token=Header(None)):
    return add_category_service(category, x_token)


@login_required
@app.put(f"{base_url}" + "/category/")
async def category_edition(category: CategoryRequestDTO, x_token: Annotated[str | None, Header()] = None):
    return edit_category_service(category, x_token)


@login_required
@app.delete(f"{base_url}" + "/category/{category_id}")
async def category_deletion(category_id, x_token: Annotated[str | None, Header()] = None):
    return delete_category_service(category_id)


@login_required
@app.get(f"{base_url}" + "/category/")
async def category_list(x_token: Annotated[str | None, Header()] = None):
    return get_categories(token_parser(x_token))


@app.exception_handler(ApiException)
async def api_exception_handler(request: Request, exc: ApiException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"{exc.message} ",
                 "request": f"{dict(request.path_params)},{dict(request.query_params)},{dict(request)}"},
    )

if category_empty():
    create_category(Category(color=None, icon=None, title="food", user_id="golbal"))
    create_category(Category(color=None, icon=None, title="school", user_id="golbal"))
    create_category(Category(color=None, icon=None, title="work", user_id="golbal"))
    create_category(Category(color=None, icon=None, title="cloths", user_id="golbal"))
run(app, host="0.0.0.0", port=8023)
