import os, json
from flask import jsonify, make_response

script_dir = os.path.dirname(__file__)
file_path = os.path.join(script_dir, "response.json")
data_object = open(file_path, "r")
responsedetails = json.load(data_object)


def get_response(module_code, data, http_code):
    response = {
        "module_code": module_code,
        "status": "success" if http_code == 200 else "failure",
        "message": responsedetails["responseCodeData"]["succCode"][module_code]
        if http_code == 200
        else responsedetails["responseCodeData"]["errCode"][module_code],
        "code": http_code,
    }
    if data != None:
        response["data"] = data
    return make_response(jsonify(response), http_code)
