from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.database_models import Base

db_path = "postgresql://postgres:a2bf9c79@localhost:5432/todo-api"

engine = create_engine(db_path)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Creates all tables if they don't exist."""
    Base.metadata.create_all(engine)

def get_session():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()