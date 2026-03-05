from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)


class Website(Base):
    __tablename__ = "websites"

    id = Column(Integer, primary_key=True)
    domain = Column(String)
    user_id = Column(Integer)
