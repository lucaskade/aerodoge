import sqlite3
from config import DB_PATH

def create_db():
    """Create the SQLite database and table if not exist."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drone_status (
            drone_id INTEGER PRIMARY KEY,
            status TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def insert_drone_status(drone_id, status):
    """Insert a new drone status into the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO drone_status (drone_id, status) VALUES (?, ?)
    """, (drone_id, status))
    conn.commit()
    conn.close()

def get_drone_status(drone_id):
    """Get the status of a drone from the database."""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM drone_status WHERE drone_id = ?
    """, (drone_id,))
    result = cursor.fetchone()
    conn.close()
    return result
