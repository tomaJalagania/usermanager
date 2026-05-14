from flask import Flask,jsonify
from mymodels import User,Base
from db import DB


app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://user:12345678@localhost/users"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
db = DB(dburi=app.config.get("SQLALCHEMY_DATABASE_URI"),app=app)


@app.route("/")
def home():
   res = db.get_all_users()
   return jsonify(res)

@app.route("/add/<user>")
def add_user(user):
     user = User(Username="toma",Email="toma@gmail.com")
     db.create_eng()
     db.add_user(user=user)
     return "success"
if __name__ == "__main__":
    
    app.run(host="0.0.0.0",debug=True)