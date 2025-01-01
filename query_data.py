import sqlite3
import pandas as pd

DB_FILE = "challenge.db"

def fetch_data():
    with sqlite3.connect(DB_FILE) as conn:
        session_sources = pd.read_sql("SELECT * FROM session_sources", conn)
        conversions = pd.read_sql("SELECT * FROM conversions", conn)
    return session_sources, conversions

if __name__ == "__main__":
    session_sources, conversions = fetch_data()
    print("Session Sources:")
    print(session_sources.head())
    print("Conversions:")
    print(conversions.head())