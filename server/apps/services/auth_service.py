import jwt
import datetime
from apps.config.Environment import environment


def create_jwt(user_id):
    expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

    payload = {
        "user_id": user_id,
        "exp": expiration_time
    }

    token = jwt.encode(payload, environment.jwt_secret, algorithm="HS256")
    return token


def verify_jwt(token):
    try:
        jwt.decode(token, environment.jwt_secret, algorithms=["HS256"])
        return True

    except jwt.ExpiredSignatureError:
        print("Expired token")
        return False
    except jwt.InvalidTokenError:
        return False
