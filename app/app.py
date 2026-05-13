from flask import Flask,jsonify
from mymodels import User,Base
from db import create_eng,add_user


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://user:12345678@localhost/users"
eng = create_eng(app)


@app.route("/")
def home():
    
    
    user = User(Username="maka",Email="jassdsasssm@gmail.com")
    
    res = add_user(user,eng)
    if res["msg"] == "success":
        data = {
           "msg":"success",
            "Username":res["user"].Username
        }
    else:
        data = {
            "msg":"email is exit"
        }
    return jsonify(data)
if __name__ == "__main__":
    Base.metadata.create_all(bind=eng)
    app.run(host="0.0.0.0")