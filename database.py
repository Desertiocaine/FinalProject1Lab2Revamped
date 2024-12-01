import sqlite3
from sqlite3 import Connection
from typing import Optional, List, Tuple

def create_connection(db_file: str) -> Optional[Connection]:
    """
    Create a database connection to the SQLite database.

    Args:
        db_file (str): The database file name.

    Returns:
        Optional[Connection]: SQLite connection object, or None if an error occurs.
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)  # Establish connection to the database
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")  # Print error message if connection fails
    return conn

def create_table(conn: Connection) -> None:
    """
    Create a table if it doesn't exist.

    Args:
        conn (Connection): SQLite connection object.
    """
    try:
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL,
                grade TEXT NOT NULL
            );
        ''')  # SQL statement to create a table
        conn.commit()  # Commit changes
        print("Table created successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")  # Print error message if creation fails

def add_student(conn: Connection, score: int, grade: str) -> None:
    """
    Insert a new student's score and grade.

    Args:
        conn (Connection): SQLite connection object.
        score (int): Student's score.
        grade (str): Corresponding grade for the score.
    """
    try:
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute(
            'INSERT INTO students (score, grade) VALUES (?, ?)',
            (score, grade)
        )  # SQL statement to insert a new record
        conn.commit()  # Commit changes
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")  # Print error message if insertion fails

def get_all_students(conn: Connection) -> List[Tuple[int, int, str]]:
    """
    Retrieve all students from the database.

    Args:
        conn (Connection): SQLite connection object.

    Returns:
        List[Tuple[int, int, str]]: List of tuples containing student ID, score, and grade.
    """
    try:
        cursor = conn.cursor()  # Create a cursor object
        cursor.execute('SELECT * FROM students')  # SQL statement to select all records
        return cursor.fetchall()  # Return all rows of the query result
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")  # Print error message if retrieval fails
        return []