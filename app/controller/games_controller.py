from database import Games
from response import get_response


def get_game_controller(gameids, titles, platforms, genres, scores, editors_choice):
    try:
        games_filters = []
        if gameids:
            games_filters.append(Games.gameid.in_(gameids))
        if titles:
            games_filters.append(Games.title.in_(titles))
        if platforms:
            games_filters.append(Games.platform.in_(platforms))
        if genres:
            games_filters.append(Games.genre.in_(genres))
        if scores:
            games_filters.append(Games.score.in_(scores))
        if editors_choice!=None:
            games_filters.append(Games.editors_choice == editors_choice)
        games_details = Games().fetch(games_filters).all()
        if len(games_details) == 0:
            return get_response("GAME_ERR005", None, 409)
        games_details_json = []
        for d in games_details:
            d.__dict__.__delitem__('_sa_instance_state')
            games_details_json.append(d.__dict__)
        return get_response("GAME_RES001", games_details_json, 200)
    except Exception:
        raise


def add_game_controller(game_details):
    try:
        game_duplicate_filter = [
            Games.title == game_details["title"]
        ]
        game = Games().fetch(game_duplicate_filter).first()
        if game:
            return get_response("GAME_ERR006", None, 409)
        add_game_details = Games().add(game_details)
        add_game_details.__dict__.__delitem__('_sa_instance_state')
        return get_response("GAME_RES002", add_game_details.__dict__, 200)
    except Exception:
        raise

def edit_game_controller(game_details):
    try:
        if 'title' in game_details:
            game_duplicate_filter = [
                Games.gameid != game_details["gameid"],
                Games.title == game_details["title"]
            ]
            game = Games().fetch(game_duplicate_filter).first()
            if game:
                return get_response("GAME_ERR006", None, 409)
        game_filter = [
            Games.gameid == game_details.pop("gameid")
        ]
        edit_game_details = Games().edit(game_filter, game_details)
        return get_response("GAME_RES003", edit_game_details, 200)
    except Exception:
        raise

def delete_game_controller(gameid):
    try:
        game_filter = [
            Games.gameid == gameid
        ]
        Games().delete(game_filter)
        return get_response("GAME_RES004", None, 200)
    except Exception:
        raise
