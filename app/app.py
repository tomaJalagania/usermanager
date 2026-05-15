from flask import Flask,jsonify,request
from flask_cors import CORS
from mymodels import User,Base
from db import DB
import os



#================= Load VARIABLES ============================
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB=os.getenv("POSTGRES_DB")
POSTGRES_HOST = os.getenv("POSTGRES_SERVER_NAME")
#=============================================================

app = Flask(__name__)
CORS(app=app)
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql+psycopg2://user:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = DB(dburi=app.config.get("SQLALCHEMY_DATABASE_URI"),app=app)


@app.route("/users")
def home():
   res = db.get_all_users()
   return jsonify(res)

@app.route("/add",methods=["POST"])
def add_user():
     data = request.get_json()
     user = User(Username=data["Username"],Email=data["Email"])
     res = db.add_user(user=user)
     return jsonify(res)


@app.route("/del",methods=["POST"])
def delete_user():
    req = request.get_json()
    id = req["id"]
    res = db.delete_user(id)
    return jsonify(res)


if __name__ == "__main__":
    
    app.run(host="0.0.0.0")