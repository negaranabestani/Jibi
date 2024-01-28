from typing import Annotated

from fastapi import FastAPI, Header, Request
from fastapi.responses import JSONResponse

from app.api.request_dto import RecordRequestDTO
from app.exception.api_exception import ApiException

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
    pass


@app.post(f"{base_url}" + "/signin/{email}")
async def sign_in(email, password):
    pass


@login_required
@app.post(f"{base_url}" + "/record/")
async def record_insertion(record: RecordRequestDTO, x_token: Annotated[str | None, Header()] = None):
    pass


@login_required
@app.put(f"{base_url}" + "/record/{record_id}")
async def record_edition(record_id, record: RecordRequestDTO, x_token: Annotated[str | None, Header()] = None):
    pass


@login_required
@app.delete(f"{base_url}" + "/record/{record_id}")
async def record_deletion(record_id, x_token: Annotated[str | None, Header()] = None):
    pass


@app.exception_handler(ApiException)
async def api_exception_handler(request: Request, exc: ApiException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"{exc.message} ", "request": f"{request.body()}"},
    )
