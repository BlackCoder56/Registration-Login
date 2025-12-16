from flask import Flask
from flask import request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import db

app = Flask(__name__)
CORS(app, supports_credentials=True) # -> allows cookies to be sent cross-origin

app.config["SECRET_KEY"] = "abc1234" # -> required for sessions
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db" # -> creates a file called users.db

# db = SQLAlchemy(app)
db.init_app(app) # -> initialize the db with the app
