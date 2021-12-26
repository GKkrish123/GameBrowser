from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from csv import DictReader
from config import (
    SQL_DB_SYSTEM,
    DB_USERNAME,
    DB_PASSWORD,
    DB_SERVER,
    DB_HOST,
    DB_PORT,
)

db_string = (
    f"{SQL_DB_SYSTEM}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SERVER}"
)

db = create_engine(db_string)
base = declarative_base()


class Games(base):
    __tablename__ = "games"

    gameid = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    platform = Column(String(100), nullable=False)
    genre = Column(String(100), nullable=False)
    score = Column(String(100), nullable=False)
    editors_choice = Column(Boolean, nullable=False)

class Users(base):
    __tablename__ = "users"

    userid = Column(Integer, primary_key=True, autoincrement=True)
    firstname = Column(String(100), nullable=False)
    lastname = Column(String(100), nullable=False)
    username = Column(String(100), nullable=False)
    password = Column(String(100), nullable=False)

# LOAD CSV DATA TO UPLOAD INTO DATABASE
csv_file_data = DictReader(open("games_data.csv"))
objects = []
for data in csv_file_data:
    data["editors_choice"] = True if data["editors_choice"]=="Y" else False
    objects.append(Games(**data))


def create_mock_tables(session=None):
    try:
        base.metadata.create_all(db)
        if not session:
            Session = sessionmaker(db)
            session = Session()
        session.bulk_save_objects(objects)
        session.commit()
        session.close()
    except Exception:
        raise


def delete_mock_tables():
    try:
        base.metadata.drop_all(db)
    except Exception:
        raise


if __name__ == "__main__":
    create_mock_tables()
    print("\n! MOCK TABLES CREATED SUCCESSFULLY !")
