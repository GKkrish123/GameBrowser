import os
from flask_restx import Api
from database.db_conn import create_db_engine
from flask import Flask
from route import games_route, mockdb_route, login_route

# CREATE ENGINE AT THE BEGINNING
class MyFlaskApp(Flask):
  def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    if not self.debug or os.getenv('WERKZEUG_RUN_MAIN') == 'true':
      with self.app_context():
        create_db_engine()
    super(MyFlaskApp, self).run(host=host, port=port, debug=debug, load_dotenv=load_dotenv, **options)

# CREATE FLASK APP
flask_app = MyFlaskApp(__name__)
flask_app.config['RESTX_VALIDATE'] = True


# DESCRIPTION OF APP
app_description = """
        Consists of **GAME BROWSER APIs** which performs **server-side** operations.
    """

authorizations = {
    'apikey': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'API-Key'
    }
}

# CREATE API ROUTER
api = Api(
    app=flask_app,
    title="GAME BROWSER",
    description=app_description,
    version="1.0.0",
    authorizations=authorizations
)

# CLEAR DEFAULT NAMESPACES
api.namespaces.clear() 

# ADD API NAMESPACES
api.add_namespace(login_route.login_api)
api.add_namespace(games_route.games_api)
api.add_namespace(mockdb_route.mockdb_api)

# APP START
if __name__ == "__main__":
    flask_app.run(host="0.0.0.0", port=5000)
