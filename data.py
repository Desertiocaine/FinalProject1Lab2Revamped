from typing import List


def get_student_scores(num_students: int) -> List[int]:
    """
    Ask the user to enter scores for a given number of students.

    Args:
        num_students (int): The number of students to enter scores for.

    Returns:
        List[int]: A list containing student scores.
    """
    while True:
        try:
            # Prompt user to enter scores separated by commas
            scores_input = input(f"Enter {num_students} score(s), separated by commas: ").split(',')

            # Convert input to integers, stripping any whitespace
            scores = list(map(lambda x: int(x.strip()), scores_input))

            # Validate: Check if the number of scores matches the number of students
            if len(scores) != num_students:
                raise ValueError("Number of scores does not match the number of students.")

            # Validate: Ensure each score is between 0 and 100
            if any(score < 0 or score > 100 for score in scores):
                raise ValueError("Scores must be between 0 and 100.")

            # If validation passes, return the scores
            return scores

        except ValueError as e:
            # Handle invalid input: Inform user and ask for input again
            print(f"Invalid input: {e}. Please enter comma-separated integers between 0 and 100.")