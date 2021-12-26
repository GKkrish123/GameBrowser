from distutils.util import strtobool
import base64
from functools import wraps
from flask import request
from flask_restx import Namespace
from database import create_db_session
from response import get_response


SECRET_KEY = "CODE IS GOD"

# METADATA TAGS FOR SWAGGER AND DOCS
tags_metadata_description = {
    "games": "Contains all API's related to games",
    "mockdb": "Contains all API's related to mockdb",
    "login": "Contains all API's related to login",
}

# ADD NAMESPACE
games_api = Namespace('games', description=tags_metadata_description["games"])
mockdb_api = Namespace('mockdb', description=tags_metadata_description["mockdb"])
login_api = Namespace('login', description=tags_metadata_description["login"])

# LOGIN CHECK DECORATOR
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        try: 
            access_token = request.headers.get('API-Key')
            if SECRET_KEY != base64.b64decode(access_token.encode("ascii")).decode("ascii"):
                raise Exception("UNAUTHOURIZED")
            # CREATE DB SESSION
            create_db_session()
            return f(*args, **kwargs)
        except Exception as e:
            print(f"Error in decoding token :: {e}")
            return get_response("LOGIN_ERR001", None, 409)
    return decorated

def convert_to_bool(target_object, default_val):
    if target_object is None:
        return default_val
    try:
        return strtobool(target_object)
    except:
        return default_val