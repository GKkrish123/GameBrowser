from route import games_api
from flask_restx import fields

add_game_model = games_api.model('add_game_model', 
{
"title": fields.String(required=True),
"platform": fields.String(required=True),
"genre": fields.String(required=True),
"score": fields.String(required=True),
"editors_choice": fields.Boolean(required=True)
})

edit_game_model = games_api.model('edit_game_model', 
{
"title": fields.String(),
"platform": fields.String(),
"genre": fields.String(),
"score": fields.String(),
"editors_choice": fields.Boolean()
})
