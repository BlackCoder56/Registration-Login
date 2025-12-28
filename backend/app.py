from flask import Flask
from flask import request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from models import db, User
from config import Config

app = Flask(__name__)
CORS(app, supports_credentials=True) # -> allows cookies to be sent cross-origin

app.config.from_object(Config) # -> load config from Config class

# db = SQLAlchemy(app)
db.init_app(app) # -> initialize the db with the app

@app.route("/register", methods=["POST"])
def register():
    data = request.json # -> Vue sends JSON data

    if User.query.filter_by(username=data["username"]).first(): # -> check if user exists to prevent duplicate accounts
        return jsonify({"error": "User already exists"}), 400

    new_user = User(
        username=data["username"], 
        password=data["password"]
        ) # -> create new user instance
    
    db.session.add(new_user) # -> prepare to save
    db.session.commit() # -> save to database

    return jsonify({"message": "Registration successful"}) # -> Sends response back to Vue

@app.route("/login", methods=["POST"])
def login():
    data = request.json

    user = User.query.filter_by(username=data["username"]).first() # -> find user by username in Database

    if user and user.password == data["password"]: # -> check user exists & password matches
        session["user_id"] = user.id # ->"" Creates a session for logged in user, flask stores user ID, Browser stores a cookie, User is now logged in
        return jsonify({"message": "Login successful"})
    
    return jsonify({"error": "Invalid username or password"}), 401


"""sumary_line

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
"""
