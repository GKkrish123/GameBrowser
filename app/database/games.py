from sqlalchemy import Column, String, Integer, Boolean
from .base import base


class Games(base):
    gameid = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(100), nullable=False)
    platform = Column(String(100), nullable=False)
    genre = Column(String(100), nullable=False)
    score = Column(String(100), nullable=False)
    editors_choice = Column(Boolean, nullable=False)
