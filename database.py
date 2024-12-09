import sqlite3
import configparser
import json
from typing import List, Optional, Tuple

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
        self.cursor = self.conn.cursor()

    def create_connection(self) -> Optional[sqlite3.Connection]:
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
            cursor.execute('DROP TABLE IF EXISTS students')  # Drop the existing table
            cursor.execute('''
                CREATE TABLE students (
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    student_id TEXT UNIQUE NOT NULL,
                    scores TEXT NOT NULL,
                    final_grade REAL NOT NULL,
                    grade_letter TEXT NOT NULL
                );
            ''')
            self.conn.commit()
            print("Table creation attempted successfully")  # Debugging
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def add_student(self, first_name: str, last_name: str, student_id: str, scores: List[int], final_grade: float, grade_letter: str) -> None:
        """
        Insert a new student's first name, last name, student ID, scores, final grade, and grade letter into the database.

        Args:
            first_name (str): Student's first name.
            last_name (str): Student's last name.
            student_id (str): Unique student ID.
            scores (List[int]): List of student scores.
            final_grade (float): Calculated final grade.
            grade_letter (str): Calculated letter grade.
        """
        try:
            scores_json = json.dumps(scores)  # Convert scores list to JSON string
            cursor = self.conn.cursor()
            cursor.execute(
                '''
                INSERT INTO students (first_name, last_name, student_id, scores, final_grade, grade_letter)
                VALUES (?, ?, ?, ?, ?, ?)
                ''',
                (first_name, last_name, student_id, scores_json, final_grade, grade_letter)
            )
            self.conn.commit()
        except sqlite3.IntegrityError:
            raise
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")

    def get_all_students(self) -> List[Tuple[str, str, str, str, float, str]]:
        """
        Retrieve all student records from the database.

        Returns:
            List[Tuple[str, str, str, str, float, str]]: List of tuples containing student records.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute('SELECT * FROM students')
            results = cursor.fetchall()
            print("Retrieved data:", results)  # Debugging output
            return results
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred")
            return []

    def close_connection(self) -> None:
        if self.conn:
            self.conn.close()

if __name__ == '__main__':
    # Create an instance of the database handler
    db_handler = DatabaseHandler()

    # Call the create_table method to ensure the table is created
    db_handler.create_table()

    # Optional: Print a message to confirm execution
    print("Checked table creation successfully.")