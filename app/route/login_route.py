from flask import request
from flask_restx import Resource
from controller import login_service_controller, signup_controller
from response import get_response
from database import create_db_session
from request import user_login_model, signup_model
from . import login_api, SECRET_KEY


@login_api.route("/")
class Login(Resource):
    @login_api.doc(responses={ 200: 'Success', 409: 'Failure'})
    @login_api.expect(user_login_model)
    def post(self):
        """ LOGIN TO THE GAME BROWSER """
        try:
            create_db_session()
            user_login_details = request.get_json()
            return login_service_controller(user_login_details, SECRET_KEY)
        except Exception as e:
            print("login exception : ", e)
            return get_response("LOGIN_ERR002", None, 409)

@login_api.route("/signup/")
class Signup(Resource):
    @login_api.doc(responses={ 200: 'Success', 409: 'Failure'})
    @login_api.expect(signup_model)
    def post(self):
        """ SIGNUP TO THE GAME BROWSER """
        try:
            create_db_session()
            user_details = request.get_json()
            return signup_controller(user_details)
        except Exception as e:
            print("signup exception : ", e)
            return get_response("SIGNUP_ERR001", None, 409)