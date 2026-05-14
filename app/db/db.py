from sqlalchemy import create_engine,insert,select
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from mymodels import Base,User

class DB:
    def __init__(self,dburi,app):
        
        
        self._dburi = dburi
        self._app = app
        self.create_eng()
        Base.metadata.create_all(self.engine)
    
    def create_eng(self):
         self.engine = create_engine(self._dburi)
         
    
    def add_user(self,user):
         
         try:
              with Session(self.engine) as session:
                   session.add(user)
                   session.commit()
         except IntegrityError as e:
              pass
    def get_all_users(self):
          try:
               with Session(self.engine) as session:
                    result = session.query(User).all()
                    return result
          except IntegrityError as e:
               pass
