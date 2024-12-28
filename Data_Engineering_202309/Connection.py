import sqlite3

class DatabaseConnection:
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = self.connect_db()

    def connect_db(self):
        try:
            conn = sqlite3.connect(self.db_file)
            print(f"Connected to database: {self.db_file}")
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def read_sql_file(self, sql_file):
        try:
            with open(sql_file, 'r') as file:
                sql_script = file.read()
            return sql_script
        except Exception as e:
            print(f"Error reading SQL file: {e}")
            return None

    def execute_sql_script(self, sql_script):
        try:
            cursor = self.conn.cursor()
            cursor.executescript(sql_script)
            print("SQL script executed successfully. Tables created or already exist.")
            self.conn.commit()
        except sqlite3.Error as e:
            print(f"Error executing SQL script: {e}")

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Database connection closed.")

def create_tables_from_sql(db_file, sql_file):
    db = DatabaseConnection(db_file)
    sql_script = db.read_sql_file(sql_file)
    if sql_script:
        db.execute_sql_script(sql_script)
    db.close_connection()

# Specify the database file and SQL script file
db_file = "challenge/challenge.db"  # Path to your SQLite database file
sql_file = "Data_Engineering_202309/challenge_db_create.sql"  # Path to your .sql file

# Call the function
create_tables_from_sql(db_file, sql_file)