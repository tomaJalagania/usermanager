from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,MappedAsDataclass
from dataclasses import dataclass


class Base(DeclarativeBase):
   pass

@dataclass
class User(Base):
    id: int
    Username: str
    Email: str
     
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    Username:Mapped[str]
    Email:Mapped[str] = mapped_column(unique=True)

def create_table():
    Base.metadata.create_all()