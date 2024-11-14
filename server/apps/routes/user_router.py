from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from starlette import status

from apps.models.request_model import Login
from apps.schemas.schema import Users
from apps.services import auth_service

router = APIRouter()


@router.post("/login")
def try_login(login: Login):
    user = Users.find_by_id_and_pw(user_id=login.id, user_pw=login.pw)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    token = auth_service.create_jwt(user['user_id'])

    response = JSONResponse(status_code=200, content="ok")
    response.set_cookie(key="token", value=token, max_age=3600)

    return response





@router.get("/logout")
def try_logout():
    return {"message": "Logout"}


@router.get("/settings")
def get_user_settings():
    return {"message": "setting"}