from sqlalchemy import create_engine
from sqlalchemy.orm import Session

def create_eng(app):
    db = create_engine(app.config.get("SQLALCHEMY_DATABASE_URI"))
    return db

def add_user(user, eng):
    with Session(eng) as session:
        session.add(user)
        session.commit()