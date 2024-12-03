import sqlite3
import configparser
from sqlite3 import Connection
from typing import Optional, List, Tuple

class DatabaseHandler:
    """
    Handles database operations for storing and retrieving student scores and grades.
    """

    def __init__(self):
        """
        Initialize the database handler with the database name from config.ini.
        """
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.db_name = config['Database']['name']
        self.conn = self.create_connection()

    def create_connection(self) -> Optional[Connection]:
        """
        Create a database connection to the SQLite database.

        Returns:
            Optional[Connection]: SQLite connection object or None if an error occurs.
        """
        try:
            conn = sqlite3.connect(self.db_name)
            print("Connection to SQLite DB successful")
            return conn
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
            return None

    def create_table(self) -> None:
        """
        Create the students table if it does not already exist.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL UNIQUE,
                    score INTEGER NOT NULL,
                    grade TEXT NOT NULL
                );
            ''')
            self.conn.commit()
            print("Table created successfully")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def add_student(self, name: str, score: int, grade: str) -> None:
        """
        Insert a new student's name, score, and grade into the database.

        Args:
            name (str): Student's name.
            score (int): Student's score.
            grade (str): Corresponding grade for the score.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute(
                'INSERT INTO students (name, score, grade) VALUES (?, ?, ?)',
                (name, score, grade)
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            print(f"Error: Student name '{name}' already exists.")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def get_all_students(self) -> List[Tuple[int, str, int, str]]:
        """
        Retrieve all student records from the database.

        Returns:
            List[Tuple[int, str, int, str]]: List of tuples containing student records.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM students')
            return cursor.fetchall()
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
            return []