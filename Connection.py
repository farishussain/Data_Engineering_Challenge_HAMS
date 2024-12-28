import logging
from DB_Connection import DatabaseConnection

def create_tables_from_sql(db_file, sql_file):
    db = DatabaseConnection(db_file)
    sql_script = db.read_sql_file(sql_file)
    if sql_script:
        db.execute_sql_script(sql_script)
    db.close_connection()

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Specify the database file and SQL script file
db_file = "challenge.db"  # Path to your SQLite database file
sql_file = "challenge_db_create.sql"  # Path to your .sql file

# Call the function
create_tables_from_sql(db_file, sql_file)