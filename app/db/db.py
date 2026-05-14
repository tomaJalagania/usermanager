from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from mymodels import Base

class DB:
    def __init__(self,dburi,app):
        Base.metadata.create_all()
        self._dburi = dburi
        self._app = app
    
    
    def create_eng(self):
         self.engine = create_engine(self.app.config.get("SQLALCHEMY_DATABASE_URI")):
         
    
    def add_user(self,user):
         
         try:
              with Session(self.engine) as session:
                   session.add(user)
                   session.commit()
         except IntegrityError as e:
              pass

