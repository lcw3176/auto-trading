from fastapi import APIRouter, Response, HTTPException
from starlette import status

from apps.models.request_model import Login
from apps.schemas.schema import Users
from apps.services import auth_service

router = APIRouter()


@router.post("/login")
def try_login(login: Login, response: Response):
    user = Users.find_by_id_and_pw(user_id=login.id, user_pw=login.pw)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    token = auth_service.create_jwt(user['user_id'])

    response.set_cookie(key="token", value=token)

    return Response(status_code=status.HTTP_200_OK)





@router.get("/logout")
def try_logout():
    return {"message": "Logout"}


@router.get("/settings")
def get_user_settings():
    return {"message": "setting"}