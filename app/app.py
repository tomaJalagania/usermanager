from flask import Flask,jsonify,request
from flask_cors import CORS
from mymodels import User,Base
from db import DB


app = Flask(__name__)
CORS(app=app)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://user:12345678@localhost/users"
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
    
    app.run(host="0.0.0.0",debug=True)