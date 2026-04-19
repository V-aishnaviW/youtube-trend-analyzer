# src/db.py
import sqlite3
from contextlib import contextmanager

DB_PATH = "youtube_trends.db"

def init_db():
    """Initialize DB and enable WAL mode to prevent locks"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("PRAGMA journal_mode=WAL;")
        conn.commit()

@contextmanager
def get_connection():
    """Context manager for DB connection"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
        conn.commit()
    finally:
        conn.close()