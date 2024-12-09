from typing import List

class StudentDataHandler:
    """
    Handle and validate student data including names and scores.
    """

    def __init__(self):
        self.existing_names = set()

    def get_student_data(self, num_students: int) -> List[dict]:
        """
        Collect and validate student names and scores from user input.

        Args:
            num_students (int): The number of students to enter data for.

        Returns:
            List[dict]: A list of dictionaries containing student names and scores.
        """
        students = []
        for _ in range(num_students):
            while True:
                try:
                    # Input and validate student name
                    name = input("Enter student name: ").strip()
                    if not name or name in self.existing_names:
                        raise ValueError("Name cannot be empty or duplicated.")

                    # Input and validate score attempts
                    num_attempts = int(input("Enter number of scores: "))
                    if num_attempts < 1 or num_attempts > 4:
                        raise ValueError("Attempts must be between 1 and 4.")

                    # Input and validate scores
                    scores = self._get_scores_from_input(num_attempts)

                    # If validation passes, add student data
                    self.existing_names.add(name)
                    students.append({"name": name, "scores": scores})
                    break

                except ValueError as e:
                    print(f"Invalid input: {e}")

        return students

    def _get_scores_from_input(self, num_attempts: int) -> List[int]:
        """
        Prompt user to enter a specified number of scores and validate them.

        Args:
            num_attempts (int): Number of scores to be entered.

        Returns:
            List[int]: List of validated scores.
        """
        scores = []
        for i in range(num_attempts):
            while True:
                try:
                    score = int(input(f"Enter score {i + 1}: "))
                    if score < 0 or score > 100:
                        raise ValueError("Score must be between 0 and 100.")
                    scores.append(score)
                    break
                except ValueError as e:
                    print(f"Invalid score: {e}")
        return scores

# Example usage:
# handler = StudentDataHandler()
# student_data = handler.get_student_data(2)
# print(student_data)