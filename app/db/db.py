from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

def create_eng(app):
    db = create_engine(app.config.get("SQLALCHEMY_DATABASE_URI"))
    return db

def add_user(user, eng):
    
    try:
        with Session(eng) as session:
            session.add(user)
            session.commit()
            return {
                 "msg":"success",
                 "user": user
            }
    except IntegrityError as e:
            session.rollback()
            return {
                "msg":"email is exits"
            }