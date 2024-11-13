from fastapi import Response
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from apps.services import auth_service


class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        excluded_paths = ["/login"]

        if request.url.path not in excluded_paths:
            token = request.cookies.get("token")

            if not auth_service.verify_jwt(token):
                return Response(content="not allowed", status_code=405)

        return await call_next(request)
