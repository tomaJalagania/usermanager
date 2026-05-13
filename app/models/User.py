from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column

class Base(DeclarativeBase):
    id:Mapped[int] = mapped_column(primary_key=True)


class User(Base):
    Username:Mapped[str]
    Email:Mapped[str] = mapped_column(unique=True)
