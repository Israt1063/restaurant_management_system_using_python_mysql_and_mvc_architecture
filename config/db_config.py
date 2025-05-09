import mysql.connector

DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'foodiehub_db'
}

def get_db_connection():
    """Establish and return database connection."""
    return mysql.connector.connect(**DB_CONFIG)
