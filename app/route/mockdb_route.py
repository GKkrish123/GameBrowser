from flask_restx import Resource
from controller import create_mock_db_tables_controller, delete_mock_db_tables_controller
from response import get_response
from . import mockdb_api


@mockdb_api.route("/")
class MockDB(Resource):
    @mockdb_api.doc(responses={ 200: 'Success', 409: 'Failure'})
    def post(self):
        """ ADD MOCK TABLES AND VALUES INTO THE DATABASE """
        try:
            return create_mock_db_tables_controller()
        except Exception as e:
            print("create_mock_db_tables exception : ", e)
            return get_response("MOCK_ERR001", None, 409)

    @mockdb_api.doc(responses={ 200: 'Success', 409: 'Failure'})
    def delete(self):
        """ DELETE THE MOCK TABLES AND VALUES FROM THE DATABASE """
        try:
            return delete_mock_db_tables_controller()
        except Exception as e:
            print("delete_mock_db_tables exception : ", e)
            return get_response("MOCK_ERR002", None, 409)
