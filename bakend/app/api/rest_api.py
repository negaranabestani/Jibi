from typing import Annotated

from fastapi import FastAPI, Header, Request
from fastapi.responses import JSONResponse

from app.entity.expense import Expense
from app.exeption.api_exception import ApiException

app = FastAPI()

base_url = "/jibi"


@app.post(f"{base_url}"+"/signup/{email}")
async def sign_up(email, username, password):
    pass


@app.post(f"{base_url}"+"/signup/{email}")
async def sign_up(email, password):
    pass


@app.post(f"{base_url}"+"/expense-insertion/")
async def expense_insertion(expense: Expense, x_token: Annotated[str | None, Header()] = None):
    if x_token is None:
        raise ApiException("null token", 401)
    pass


@app.exception_handler(ApiException)
async def api_exception_handler(request: Request, exc: ApiException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": f"{exc.message} ", "request": f"{request.body()}"},
    )
