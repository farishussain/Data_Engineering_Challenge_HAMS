import sqlite3

DB_FILE = "challenge.db"
SQL_SCRIPT = "challenge_db_create.sql"

def initialize_database():
    with sqlite3.connect(DB_FILE) as conn, open(SQL_SCRIPT, "r") as sql_file:
        conn.executescript(sql_file.read())
        print("Database initialized and tables created successfully.")

if __name__ == "__main__":
    initialize_database()