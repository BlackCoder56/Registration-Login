from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # -> unique user ID
    username = db.Column(db.String(100), unique=True, nullable=False) # -> unique username
    password = db.Column(db.String(100), nullable=False) # -> stored password