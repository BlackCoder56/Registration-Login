import os

class Config:
    SECRET_KEY = "abc1234" # -> required for sessions
    SQLALCHEMY_DATABASE_URI = "sqlite:///users.db" # -> creates a file called users.db