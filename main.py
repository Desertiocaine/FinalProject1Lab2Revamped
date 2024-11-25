from grades import calculate_grades
from ui import display_grades
from database import create_connection, create_table, add_student, get_all_students


def main():
    """Main function to manage student scores and grades."""
    try:
        # Connect to the SQLite database
        connection = create_connection('students.db')
        create_table(connection)

        # Input: Number of students
        number_of_students = int(input("Total number of students: "))

        # Input: Scores separated by commas
        scores_input = input(f"Enter {number_of_students} score(s), separated by commas: ")
        student_scores = list(map(int, scores_input.split(',')))

        # Calculate grades based on scores
        student_grades = calculate_grades(student_scores)

        # Store each score and grade pair in the database
        for score, grade in zip(student_scores, student_grades):
            add_student(connection, score, grade)

        # Retrieve all stored student records and display them
        stored_students = get_all_students(connection)
        display_grades([record[1] for record in stored_students], [record[2] for record in stored_students])

    except Exception as error:
        print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
