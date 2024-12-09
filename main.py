from data import StudentDataHandler
from database import DatabaseHandler
from ui import StudentGradeApp
from grades import calculate_grades, calculate_final_grade

def main():
    """
    Main function to manage student scores and grades.
    Ensures initialization of the database and GUI,
    followed by data collection, processing, and storage.
    """
    try:
        # Initialize database
        db = DatabaseHandler()
        db.create_table()

        # Initialize UI
        app = StudentGradeApp()

        # Manage UI interactions
        app.root.mainloop()  # Run the UI loop for user interactions

        # Collect student data after the main loop ends
        first_name, last_name, student_id, student_scores = app.get_student_data()

        # Calculate final grade and letter grade
        final_grade, letter_grade = calculate_final_grade(student_scores)

        # Insert data into the database
        db.add_student(first_name, last_name, student_id, student_scores, final_grade, letter_grade)

        # Retrieve and display all stored student records
        stored_data = db.get_all_students()
        app.display_grades(stored_data)

        # Print the data to the console
        print("Stored student records:")
        for record in stored_data:
            print(record)

    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()