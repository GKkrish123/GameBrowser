from flask import request
from flask_restx import Resource
from response import get_response
from request import add_game_model, edit_game_model
from controller import get_game_controller, add_game_controller, edit_game_controller, delete_game_controller
from . import games_api, login_required, convert_to_bool


@games_api.route("/")
class GamesClass(Resource):
    @games_api.doc(security='apikey')
    @games_api.doc(responses={ 200: 'Success', 409: 'Failure'},
                   params={ 'gameids': 'Specify the Ids of the game(Comma separated)',
                            'titles': 'Specify the titles of the game(Comma separated)',
                            'platforms': 'Specify the platforms of the game(Comma separated)',
                            'genres': 'Specify the genres of the game(Comma separated)',
                            'scores': 'Specify the scores of the game(Comma separated)',
                            'editors_choice': 'Specify the editors_choice of the game(True or False)', })
    @login_required
    def get(self):
        """ FETCH GAMES FROM THE GAME BROWSER """
        try:
            gameids = request.args.get("gameids") and request.args.get("gameids").split(',')
            titles = request.args.get("titles") and request.args.get("titles").split(',')
            platforms = request.args.get("platforms") and request.args.get("platforms").split(',')
            genres = request.args.get("genres") and request.args.get("genres").split(',')
            scores = request.args.get("scores") and request.args.get("scores").split(',')
            editors_choice = convert_to_bool(request.args.get("editors_choice"), None)
            return get_game_controller(gameids, titles, platforms, genres, scores, editors_choice)
        except Exception as e:
            print("get_games exception : ", e)
            return get_response("GAME_ERR001", None, 409)

    @games_api.doc(security='apikey')
    @games_api.doc(responses={ 200: 'Success', 409: 'Failure'})
    @games_api.expect(add_game_model)
    @login_required
    def post(self):
        """ ADD GAME TO THE GAME BROWSER """
        try:
            game_details = request.get_json()
            return add_game_controller(game_details)
        except Exception as e:
            print("add_game exception : ", e)
            return get_response("GAME_ERR002", None, 409)

@games_api.route("/<int:gameid>")
class GamesbyIDClass(Resource):
    @games_api.doc(security='apikey')
    @games_api.doc(responses={ 200: 'Success', 409: 'Failure'},
			       params={ 'gameid': 'Specify the Id of the game' })
    @games_api.expect(edit_game_model)
    @login_required
    def put(self, gameid):
        """ UPDATE GAME OF THE GAME BROWSER """
        try:
            game_details = request.get_json()
            game_details["gameid"] = gameid
            return edit_game_controller(game_details)
        except Exception as e:
            print("edit_game exception : ", e)
            return get_response("GAME_ERR003", None, 409)
    
    @games_api.doc(security='apikey')
    @games_api.doc(responses={ 200: 'Success', 409: 'Failure'},
			       params={ 'gameid': 'Specify the Id of the game' })
    @login_required
    def delete(self, gameid):
        """ DELETE GAME OF THE GAME BROWSER """
        try:
            return delete_game_controller(gameid)
        except Exception as e:
            print("delete_game exception : ", e)
            return get_response("GAME_ERR004", None, 409)
