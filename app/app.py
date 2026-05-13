from flask import Flask
from mymodels import User,Base
from db import create_eng,add_user


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://user:12345678@localhost/users"
eng = create_eng(app)


@app.route("/")
def home():
    
    
    user = User(Username="maka",Email="maka.cucqiridze@gmail.com")
    add_user(user,eng)
    return "success"

if __name__ == "__main__":
    Base.metadata.create_all(bind=eng)
    app.run(host="0.0.0.0")