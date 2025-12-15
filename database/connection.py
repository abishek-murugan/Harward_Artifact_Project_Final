# database/connection.py

from sqlalchemy import create_engine
from config import DATABASE_URL

def get_engine():
    engine = create_engine(
        DATABASE_URL,
        pool_pre_ping=True,   # handles dropped connections
        echo=False
    )
    return engine
