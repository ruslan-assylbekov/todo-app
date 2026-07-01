import datetime
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

Base = declarative_base() # base for database models

class users(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    password = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    created = Column(DateTime, default=datetime.datetime.now)
    last_updated = Column(DateTime, default=datetime.datetime.now)


class tasks(Base):
    __tablename__ = 'tasks'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    text = Column(String)
    due_date = Column(DateTime, nullable=True)
    created = Column(DateTime, default=datetime.datetime.now)
    last_updated = Column(DateTime, default=datetime.datetime.now)
