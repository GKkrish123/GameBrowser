import base64
from database import Users
from response import get_response


def login_service_controller(user_details, secret_key):
    try:
        users_filter = [
            Users.username == user_details["username"],
            Users.password == base64.b64encode(user_details["password"].encode("ascii")).decode("ascii")
        ]
        user = Users().fetch(users_filter).first()
        if not user:
            return get_response("LOGIN_ERR003", None, 409)
        data = {
            "firstname": user.firstname,
            "lastname": user.lastname,
            "username": user.username,
            "token": base64.b64encode(secret_key.encode("ascii")).decode("ascii"),
            "how_to_login": "copy and paste the token inside the Authorize button and click Authorize",
            "how_to_logout": "click logout inside the Authorize tab"
        }
        return get_response("LOGIN_RES001", data, 200)
    except Exception:
        raise

def signup_controller(user_details):
    try:
        users_filter = [
            Users.username == user_details["username"]
        ]
        user = Users().fetch(users_filter).first()
        if user:
            return get_response("SIGNUP_ERR002", None, 409)
        user_details["password"] = base64.b64encode(user_details["password"].encode("ascii")).decode("ascii")
        user = Users().add(user_details)
        data = {
            "firstname": user.firstname,
            "lastname": user.lastname,
            "username": user.username
        }
        return get_response("SIGNUP_RES001", data, 200)
    except Exception:
        raise