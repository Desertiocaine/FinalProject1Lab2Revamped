import unittest
from database import DatabaseHandler
import sqlite3
import json

class TestDatabaseHandler(unittest.TestCase):
    def setUp(self):
        self.db = DatabaseHandler()
        self.db.create_table()
        self.clear_students_table()

    def clear_students_table(self):
        try:
            cursor = self.db.conn.cursor()
            cursor.execute('DELETE FROM students')
            self.db.conn.commit()
            print("Students table cleared before test.")
        except sqlite3.Error as e:
            print(f"The error '{e}' occurred while clearing the table")

    def test_add_and_retrieve_student(self):
        first_name = "Test"
        last_name = "Student"
        student_id = "12345"
        scores = [75, 85, 95]
        final_grade, grade_letter = 85.0, "B"

        self.db.add_student(first_name, last_name, student_id, scores, final_grade, grade_letter)
        students = self.db.get_all_students()

        self.assertEqual(len(students), 1)
        self.assertEqual(students[0][0], first_name)
        self.assertEqual(students[0][1], last_name)
        self.assertEqual(students[0][2], student_id)
        self.assertEqual(students[0][3], json.dumps(scores))
        self.assertEqual(students[0][4], final_grade)
        self.assertEqual(students[0][5], grade_letter)

if __name__ == "__main__":
    unittest.main()