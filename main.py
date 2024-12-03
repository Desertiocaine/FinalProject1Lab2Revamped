from database import DatabaseHandler
from data import StudentDataHandler
from ui import StudentGradeApp
from grades import calculate_grades, calculate_final_grade

def main():
    """
    Main function to manage student scores and grades.
    """
    try:
        # Initialize database
        db = DatabaseHandler('students.db')
        db.create_table()

        # Initialize UI
        app = StudentGradeApp()

        # Collect student data
        student_name, student_scores = app.get_student_data()

        # Calculate grades
        student_grades = calculate_grades(student_scores)

        # Calculate final grade
        try:
            final_grade = calculate_final_grade(student_scores)
            print(f"Student: {student_name}, Final Grade: {final_grade}")
        except ValueError as ve:
            print(f"Error calculating final grade: {ve}")
            return

        # Store data
        for score, grade in zip(student_scores, student_grades):
            db.add_student(student_name, score, grade)

        # Display all stored student records
        app.display_grades(db.get_all_students())

    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()