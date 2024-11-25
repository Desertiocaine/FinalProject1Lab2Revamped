import sqlite3
from sqlite3 import Connection
from typing import List, Tuple, Optional

def create_connection(db_file: str) -> Optional[Connection]:
    """Create a database connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print("Connection to SQLite DB successful")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
    return conn

def create_table(conn: Connection) -> None:
    """Create a table if it doesn't exist."""
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS students (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                score INTEGER NOT NULL,
                grade TEXT NOT NULL
            );
        ''')
        conn.commit()
        print("Table created successfully")
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

def add_student(conn: Connection, score: int, grade: str) -> None:
    """Insert a new student's score and grade."""
    try:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO students (score, grade) VALUES (?, ?)', (score, grade))
        conn.commit()
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")

def get_all_students(conn: Connection) -> List[Tuple[int, int, str]]:
    """Retrieve all students from the database."""
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM students')
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"The error '{e}' occurred")
        return []