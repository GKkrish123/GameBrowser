# GAME BROWSER APP (Python/Flask)

* This project contains APIs related to features of the GAME BROWSER APP.

* Setting up the environment
  1. Visual Studio Code (`https://code.visualstudio.com/download`)
  2. Python (`https://www.python.org/downloads/`)
  3. SQL Server (Example: MySQL,PostgreSQL) (Tested with MySQL)
  4. Clone this repository into VSCode, open the CMD terminal in the installed path (inside the `GameBrowser` folder)
  5. Install `pipenv` by running the command `pip install pipenv`
  5. Create virtual environment by running the command `pipenv shell`
  6. Run the command `pipenv install --dev --skip-lock` to install all Python dependencies.

* Creating the mock database tables (MANDATORY IF YOU DON'T HAVE THE SPECIFIED TABLES IN YOUR SQL SERVER)
  1. Start your local SQL server.
  2. Apply your SQL server configuration in the `.env` file.
  3. Run the command `python mock_db_tables.py` inside `app` folder to create the mock tables in your specified SQL server.
  4. NOTE: There are also APIs for creating and deleting mock DB which can be run after deploying the App Server.

# Deploying the APP server
  * Run the command `python startup.py` inside `app` folder to start the app.
    * http://localhost:5000 -> Swagger URL
