from route import login_api
from flask_restx import fields

user_login_model = login_api.model('user_login_model', 
{
'username': fields.String(required=True),
'password': fields.String(required=True)
})

signup_model = login_api.model('signup_model', 
{
'firstname': fields.String(required=True),
'lastname': fields.String(required=True),
'username': fields.String(required=True),
'password': fields.String(required=True)
})
