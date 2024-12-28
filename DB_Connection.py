import sqlite3
import logging

class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.connect_db()

    def connect_db(self):
        try:
            conn = sqlite3.connect(self.db_file)
            logging.info(f"Connected to database: {self.db_file}")
            return conn
        except sqlite3.Error as e:
            logging.error(f"Error connecting to database: {e}")
            return None

    def read_sql_file(self, sql_file):
        try:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            return sql_script
        except Exception as e:
            logging.error(f"Error reading SQL file: {e}")
            return None

    def execute_sql_script(self, sql_script):
        try:
            cursor = self.conn.cursor()
            cursor.executescript(sql_script)
            logging.info("SQL script executed successfully. Tables created or already exist.")
            self.conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error executing SQL script: {e}")

    def close_connection(self):
        if self.conn:
            self.conn.close()
            logging.info("Database connection closed.")