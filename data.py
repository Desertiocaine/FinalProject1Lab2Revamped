from typing import List


def get_student_scores(num_students: int) -> List[int]:
    """
    Ask the user to enter scores for a given number of students.

    Args:
        num_students (int): Number of students.

    Returns:
        List[int]: List of student scores.
    """
    while True:
        try:
            scores_input = input(f"Enter {num_students} score(s), separated by commas: ").split(',')
            scores = list(map(int, scores_input))

            # Validate score count
            if len(scores) != num_students:
                raise ValueError("Number of scores does not match the number of students.")

            # Validate each score
            if any(score < 0 or score > 100 for score in scores):
                raise ValueError("Scores must be between 0 and 100.")

            return scores

        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")
