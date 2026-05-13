from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,MappedAsDataclass



class Base(DeclarativeBase):
   pass

class User(Base):
    __tablename__ = "user"
    id:Mapped[int] = mapped_column(primary_key=True)
    Username:Mapped[str]
    Email:Mapped[str] = mapped_column(unique=True)

def create_table():
    Base.metadata.create_all()