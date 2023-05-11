from sqlmodel import Session
from sqlmodel import create_engine

from src.settings import DATABASE_URL

engine = create_engine(DATABASE_URL, pool_pre_ping=True)


def db_sql_session() -> Session:
    with Session(engine, autoflush=True) as session:
        yield session
