from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.config import DB_CONNECTION_URL


engine = create_engine(DB_CONNECTION_URL, echo=True)


def get_session():
    session_class = sessionmaker(bind=engine)
    session = session_class()
    return session
