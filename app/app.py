from flask import Flask,jsonify
from mymodels import User,Base
from db import DB


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://user:12345678@localhost/users"
db = DB()


@app.route("/")
def home():
    user = User("toma","toma@gmail.com")
    db.create_eng()
    db.add_user(user=user)
    return "success"
if __name__ == "__main__":
    
    app.run(host="0.0.0.0")